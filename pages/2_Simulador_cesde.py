import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Configurar el tema de Streamlit
st.set_page_config(
    page_title="Simulador Cesde",
    page_icon=":fork_and_knife:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS para personalizar el estilo
st.markdown("""
    <style>
        .main {
            background-color: #829DC2;
            color: #02153B;
        }
        .stSelectbox label, .stButton button, .stSlider label, .stTextInput label {
            color: #02153B;
        }
        h1, h2, h3, h4 {
            color: #02153B;
        }
        .css-1ekf893 {
            background-color: #1f77b4;
        }
        .st-dx, .st-cn, .st-at {
            border: 2px solid #1f77b4;
            border-radius: 10px;
            padding: 10px;
        }
        header.css-18ni7ap {
            background-color: #0C1449;
        }
        header.css-18ni7ap .css-1v0mbdj, header.css-18ni7ap .css-1rs6os {
            color: #f0f2f6;
        }
    </style>
""", unsafe_allow_html=True)
# Título de la aplicación
st.title("Simulador Cesde")

multi = '''***Es una aplicación que permite visualizar el nivel academico que se mantiene actualmente.***

***Segun su (:red[Nivel]), (:red[Grupos]), (:red[Jornadas]) y (:red[Momentos]).***
'''
st.markdown(multi)

# Leer el archivo CSV
try:
    df = pd.read_csv('static/datasets/cesde.csv')
except FileNotFoundError:
    st.error("El archivo de datos no se encontró. Asegúrate de que el archivo esté en la ruta correcta.")
    st.stop()

# Obtener las opciones únicas de cada filtro
gruposU = sorted(df['GRUPO'].unique())
nivelesU = sorted(df['NIVEL'].unique())
jornadasU = sorted(df['JORNADA'].unique())
horarioU = sorted(df['HORARIO'].unique())
submodulosU = sorted(df['SUBMODULO'].unique())
docentesU = sorted(df['DOCENTE'].unique())
momentosU = sorted(df['MOMENTO'].unique())

# Configurar las columnas y selectores
col1, col2, col3, col4 = st.columns(4)

with col1:
    gruposU.insert(0, "Todos")
    optionGrupo = st.selectbox('Grupo', (gruposU))

with col2:       
    optionMomento = st.selectbox('Momento', (momentosU))

with col3:
    nivelesU.insert(0, "Todos")
    optionNivel = st.selectbox('Nivel', (nivelesU))

with col4:
    jornadasU.insert(0, "Todos")
    optionJornada = st.selectbox('Jornada', (jornadasU))

col5, col6 = st.columns(2)

with col5:
    submodulosU.insert(0, "Todos")
    optionSubmodulo = st.selectbox('Submódulo', (submodulosU))

# Filtrar los datos según las opciones seleccionadas
filtered_data = df
if optionGrupo != 'Todos':
    filtered_data = filtered_data[filtered_data['GRUPO'] == optionGrupo]

if optionMomento:
    filtered_data = filtered_data[filtered_data['MOMENTO'] == optionMomento]

if optionNivel != 'Todos':
    filtered_data = filtered_data[filtered_data['NIVEL'] == optionNivel]

if optionJornada != 'Todos':
    filtered_data = filtered_data[filtered_data['JORNADA'] == optionJornada]

if optionSubmodulo != 'Todos':
    filtered_data = filtered_data[filtered_data['SUBMODULO'] == optionSubmodulo]

# Crear el gráfico de barras
if not filtered_data.empty:
    NOTAS = filtered_data['NOMBRE']
    fig = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=NOTAS, y=filtered_data['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=NOTAS, y=filtered_data['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=NOTAS, y=filtered_data['PRODUCTO'])
    ])
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("No hay datos disponibles para los filtros seleccionados.")

# Gráfico  1: Conocimiento, Desempeño y Producto por Nivel
if not filtered_data.empty:
    numeric_columns = ['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']
    grouped_data = filtered_data.groupby('NIVEL')[numeric_columns].mean()
    fig2 = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=grouped_data.index, y=grouped_data['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=grouped_data.index, y=grouped_data['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=grouped_data.index, y=grouped_data['PRODUCTO'])
    ])
    fig2.update_layout(barmode='stack')
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico 2: Momentos
if not filtered_data.empty:
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=filtered_data['MOMENTO'], y=filtered_data['CONOCIMIENTO'], mode='lines+markers', name='CONOCIMIENTO'))
    fig3.add_trace(go.Scatter(x=filtered_data['MOMENTO'], y=filtered_data['DESEMPEÑO'], mode='lines+markers', name='DESEMPEÑO'))
    fig3.add_trace(go.Scatter(x=filtered_data['MOMENTO'], y=filtered_data['PRODUCTO'], mode='lines+markers', name='PRODUCTO'))
    st.plotly_chart(fig3, use_container_width=True)

# Gráfico 3: distribución de estudiantes por nivel
if not filtered_data.empty:
    nivel_counts = filtered_data['NIVEL'].value_counts()
    fig4 = go.Figure(data=[go.Pie(labels=nivel_counts.index, values=nivel_counts.values)])
    st.plotly_chart(fig4, use_container_width=True)

# Crear un gráfico de barras para el rendimiento promedio por Submódulo
if optionSubmodulo == 'Todos' and not filtered_data.empty:
    grouped_data = df.groupby('SUBMODULO')[['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']].mean().reset_index()
    fig_submodulo = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=grouped_data['SUBMODULO'], y=grouped_data['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=grouped_data['SUBMODULO'], y=grouped_data['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=grouped_data['SUBMODULO'], y=grouped_data['PRODUCTO'])
    ])
    fig_submodulo.update_layout(barmode='group', title='Rendimiento promedio por Submódulo')
    st.plotly_chart(fig_submodulo, use_container_width=True)
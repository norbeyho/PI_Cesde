# import streamlit as st
# import pandas as pd
# import plotly.figure_factory as ff

# import plotly.graph_objects as go

# st.write("Simulador Cesde")
# try:
#     df = pd.read_csv('static/cesde.csv')
# except FileNotFoundError:
#     st.error("El archivo de datos no se encontró. Asegúrate de que el archivo esté en la ruta correcta.")
#     st.stop()

# # Obtener las opciones únicas de cada filtro
# gruposU = sorted(df['GRUPO'].unique())
# nivelesU = sorted(df['NIVEL'].unique())
# jornadasU = sorted(df['JORNADA'].unique())
# horarioU = sorted(df['HORARIO'].unique())
# submodulosU = sorted(df['SUBMODULO'].unique())
# docentesU = sorted(df['DOCENTE'].unique())
# momentosU = sorted(df['MOMENTO'].unique())

# # Configurar las columnas y selectores
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     gruposU.insert(0,"Todos")
#     optionGrupo = st.selectbox('Grupo', (gruposU))

# with col2:       
#     optionMomento = st.selectbox('Momento', (momentosU))

# with col3:
#     nivelesU.insert(0, "Todos")
#     optionNivel = st.selectbox('Nivel', (nivelesU))

# with col4:
#     jornadasU.insert(0, "Todos")
#     optionJornada = st.selectbox('Jornada', (jornadasU))

# # Filtrar los datos según las opciones seleccionadas
# filtered_data = df
# if optionGrupo != 'Todos':
#     filtered_data = filtered_data[filtered_data['GRUPO'] == optionGrupo]

# if optionMomento:
#     filtered_data = filtered_data[filtered_data['MOMENTO'] == optionMomento]

# if optionNivel != 'Todos':
#     filtered_data = filtered_data[filtered_data['NIVEL'] == optionNivel]

# if optionJornada != 'Todos':
#     filtered_data = filtered_data[filtered_data['JORNADA'] == optionJornada]

# # Crear el gráfico de barras
# if not filtered_data.empty:
#     NOTAS = filtered_data['NOMBRE']
#     fig = go.Figure(data=[
#         go.Bar(name='CONOCIMIENTO', x=NOTAS, y=filtered_data['CONOCIMIENTO']),
#         go.Bar(name='DESEMPEÑO', x=NOTAS, y=filtered_data['DESEMPEÑO']),
#         go.Bar(name='PRODUCTO', x=NOTAS, y=filtered_data['PRODUCTO'])
#     ])
#     fig.update_layout(barmode='group')
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.write("No hay datos disponibles para los filtros seleccionados.")

# # Crear gráficos adicionales según sea necesario
# # Ejemplo: Gráfico de barras apiladas para Conocimiento, Desempeño y Producto por Nivel
# if not filtered_data.empty:
#     grouped_data = filtered_data.groupby('NIVEL').mean()
#     fig2 = go.Figure(data=[
#         go.Bar(name='CONOCIMIENTO', x=grouped_data.index, y=grouped_data['CONOCIMIENTO']),
#         go.Bar(name='DESEMPEÑO', x=grouped_data.index, y=grouped_data['DESEMPEÑO']),
#         go.Bar(name='PRODUCTO', x=grouped_data.index, y=grouped_data['PRODUCTO'])
#     ])
#     fig2.update_layout(barmode='stack')
#     st.plotly_chart(fig2, use_container_width=True)



import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
# Set the page title and header
st.title("Simulador CESDE Bello")

df = pd.read_csv('static/datasets/cesde.csv')

gruposU = sorted(df['GRUPO'].unique())
nivelesU = sorted(df['NIVEL'].unique())
jornadasU =  sorted(df['JORNADA'].unique())
horarioU =  sorted(df['HORARIO'].unique())
submodulosU =  sorted(df['SUBMODULO'].unique())
docentesU =  sorted(df['DOCENTE'].unique())
momentosU =  sorted(df['MOMENTO'].unique())

# -----------------------------------------------------------------------------------
def filtro1():    
    col1, col2 = st.columns(2)
    with col1:
        grupo = st.selectbox("Grupo",gruposU)
    with col2:
        momento = st.selectbox("Momento",momentosU)
    resultado = df[(df['GRUPO']==grupo)&(df['MOMENTO']==momento)]
   
    resultado= resultado.reset_index(drop=True) 
    # Grafico de barras
    estudiante=resultado['NOMBRE']
    fig = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
    ])   
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    # Tabla
    st.table(resultado[["NOMBRE","CONOCIMIENTO","DESEMPEÑO","PRODUCTO"]])
    
# -----------------------------------------------------------------------------------
def filtro2():
    col1, col2, col3 = st.columns(3)
    with col1:
        grupo = st.selectbox("Grupo",gruposU)
    with col2:
        nombres = df[df['GRUPO']==grupo]
        nombre = st.selectbox("Estudiante",nombres["NOMBRE"])
    with col3:
        momentosU.append("Todos")
        momento = st.selectbox("Momento",momentosU)   

    if momento == "Todos":
        resultado = df[(df['GRUPO']==grupo)&(df['NOMBRE']==nombre)]
        # Grafico de barras
        momentos=sorted(df['MOMENTO'].unique())
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=momentos, y=resultado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=momentos, y=resultado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=momentos, y=resultado['PRODUCTO'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado= resultado.reset_index(drop=True) 
        m1 = resultado.loc[0,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        m2 = resultado.loc[1,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        m3 = resultado.loc[2,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        tm = pd.Series([m1.mean(),m2.mean(),m3.mean()])       
        st.subheader("Promedio")
        st.subheader(round(tm.mean(),1)) 
    else :   
        resultado = df[(df['GRUPO']==grupo)&(df['MOMENTO']==momento)&(df['NOMBRE']==nombre)]
        # Grafico de barras
        estudiante=resultado['NOMBRE']
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado= resultado.reset_index(drop=True) 
        conocimiento = resultado.loc[0,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        st.subheader("Promedio")
        st.subheader(round(conocimiento.mean(),1)) 
  
# -----------------------------------------------------------------------------------
filtros =[
    "Notas por grupo",
    "Notas por estudiante"
]

filtro = st.selectbox("Filtros",filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()

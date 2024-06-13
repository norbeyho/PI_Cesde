import streamlit as st

# Configurar el tema de Streamlit
st.set_page_config(
    page_title="Restaurante",
    page_icon=":fork_and_knife:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS para personalizar el estilo
st.markdown("""
    <style>
        /* Fondo y texto principal */
        .main {
            background-color: #060E3E;
            color: #f0f2f6;
        }
        /* Texto y elementos */
        .stSelectbox label, .stButton button, .stSlider label, .stTextInput label {
            color: #f0f2f6;
        }
        h1, h2, h3, h4 {
            color: #f0f2f6;
        }
        /* Títulos de los gráficos */
        .css-1ekf893 {
            background-color: #1f77b4;
        }
        .st-dx, .st-cn, .st-at {
            border: 2px solid #1f77b4;
            border-radius: 10px;
            padding: 10px;
        }
        /* Barra superior */
        header.css-18ni7ap {
            background-color: #505C72;
        }
            
        .css-1aumxhk {
        background-color: #505C72; /* Cambia el color del menú de páginas */
        
        /* Configuración y texto de la barra superior */
        header.css-18ni7ap .css-1v0mbdj, header.css-18ni7ap .css-1rs6os {
            color: #505C72;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Bienvenido a nuestro Proyecto Integrador Python")
st.image("img/fondo.jpeg")
st.markdown("""
    <div style="text-align: center; font-size: 18px; color: #F9FAFC;">
        Disfruta de nuestro contenido
    </div>
""", unsafe_allow_html=True)
st.write("Elizabeth Restrepo" )
st.write("Richard Blanco")
st.write("Norbey Hernandez")
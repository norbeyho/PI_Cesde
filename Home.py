import streamlit as st
import base64

st.title("Proyecto Integrador Python")

# Función para codificar la imagen en base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Codificar la imagen de fondo
img_base64 = get_base64_of_bin_file('fondo.jpeg')

# CSS para establecer la imagen de fondo
page_bg_img = f'''
<style>
body {{
    background-image: url("img/fondo.jpeg";base64,{img_base64}");
    background-size: cover;
    background-position: center;
}}
</style>
'''

st.image("img/fondo.jpeg", caption="Disfruta de nuestro contenido")

st.write("Elizabeth Restrepo")
st.write("Richard Blanco")
st.write("Norbey Hernandez")
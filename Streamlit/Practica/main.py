import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title='Cargatron', page_icon=':sunglasses:', layout='wide')

st.title('Cargatron')

data = pd.read_csv(r'C:\Users\Rafael Ortega\Proyectos\Data_Engineer\Streamlit\Practica\data\red_recarga_2021.csv')

st.write(data)

st.balloons()



st.file_uploader('Elige un archivo .csv', type=['csv'])

from PIL import Image


st.title('HOME')

image = Image.open(r'C:\Users\Rafael Ortega\Proyectos\Data_Engineer\Streamlit\Teoria\img\puntos-recarga-madrid.jpg')
st.image(image)

with st.expander("See explanation"):
    st.write('''Esta pagina permite encontrar los cargadores de coches electricos de España''')
    st.image("https://static.streamlit.io/examples/dice.jpg")


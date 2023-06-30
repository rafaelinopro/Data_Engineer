import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from PIL import Image


st.title('HOME')

image = Image.open(r'C:\Users\Rafael Ortega\Proyectos\Data_Engineer\Streamlit\Teoria\img\puntos-recarga-madrid.jpg')
st.image(image)

with st.expander("See explanation"):
    st.write('''Esta pagina permite encontrar los cargadores de coches electricos de España''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
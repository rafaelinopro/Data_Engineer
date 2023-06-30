import seaborn as sns
import pandas as pd
import streamlit as st
import numpy as np

# Load Dataset
df = sns.load_dataset('penguins')

# Page Title
st.title('Ejemplo de uso de st.write()')

# Text + emoji
st.write('Hola :sunglasses: :heart: ')

# Calculations
st.write(1+5)

# Variables
a = 2**3
st.write(a*5)

# Table
st.write(df.head(5))

# Multiple
st.write('st.write("text", df)', df.head(7))

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)
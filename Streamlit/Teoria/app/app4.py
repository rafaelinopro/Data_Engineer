import streamlit as st
from PIL import Image

#Insert a picture
# First, read it with PIL
image = Image.open(r'img\591e3af95df3c.jpeg')
image2 = Image.open(r'img\images.jpg')
# Load Image in the App
st.image(image)
st.image(image2)
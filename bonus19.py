import streamlit as st
from PIL import Image

camera_image = st.camera_input("camera")

if camera_image:
    img = Image.open(camera_image)
    converted_img = img.convert("L")
    st.image(converted_img)

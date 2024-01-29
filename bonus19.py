# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image


def convert_image_gray(image):
    img = Image.open(image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)


st.subheader("Color to Grayscale Converter")
upload_image = st.file_uploader("upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    convert_image_gray(camera_image)
if upload_image:
    convert_image_gray(upload_image)

import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Streamlit App
st.title('Image Text Extraction with EasyOCR')

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert the image to numpy array (EasyOCR requires numpy format)
    image_np = np.array(image)

    # Extract text using EasyOCR
    with st.spinner('Extracting text...'):
        result = reader.readtext(image_np)

    # Display extracted text
    st.subheader('Extracted Text:')
    extracted_text = "\n".join([text[1] for text in result])
    st.text(extracted_text)

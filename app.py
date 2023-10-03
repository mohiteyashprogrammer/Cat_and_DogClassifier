import streamlit as st 
from PIL import Image
import tensorflow as tf
import numpy as np

st.header("Cat and Dog Classifier")

model = tf.keras.models.load_model("C:\\Users\\yash mohite\\OneDrive\\Desktop\\Deep learning projects\\artifacts\\training\\model.h5")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:

    image = Image.open(uploaded_file)
    img = image.resize((256,256))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) # [batch_size, row, col, channel]
    result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]

    argmax_index = np.argmax(result, axis=1) # [0, 0]
    if argmax_index[0] == 0:
        st.image(image, caption="predicted: cat")
        st.header("predicted: cat")
    else:
        st.image(image, caption='predicted: dog')
        st.header("predicted: Dog")
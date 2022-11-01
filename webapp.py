import streamlit as st
from keras.models import load_model
import tensorflow as tf
from keras.utils import load_img, img_to_array
import numpy as np

def load_image(img_path):


    img = load_img(img_path, target_size=(224, 224))
    img_tensor = img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.  

    return img_tensor

# model = load_model(r"C:\Users\danie\Documentos\GitHub\RoomsClassifier\Models\model_transfer_learning\saved_model.pb")
model = load_model('Models\model_transfer_learning\model_transfer_learning.h5')
class_names = ['Bathroom', 'Bedroom', 'House Map', 'Kitchen', 'Living Room']

st.title("Room Classifier")

image_uploaded = st.file_uploader("Upload your room image",type=["jpg","png"])
if image_uploaded is not None:
    st.image(image_uploaded)

if st.button("Predict"):
    if image_uploaded is not None:
       img_tensor = load_image(image_uploaded)
       prediction =  model.predict(img_tensor)
       st.write(class_names[np.argmax(prediction)])
    else:
        st.warning("Upload a photo before making predictions")
       
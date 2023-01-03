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

st.title("Place your real estate ad")

operation = st.radio("Operation:",["Rent","Sale"])

price = st.number_input("Price",min_value=0,step=50)

city =  st.text_input("City")

road_name =  st.text_input("Road name")

images_uploaded = st.file_uploader("Upload your Images here",type=["jpg","png"],accept_multiple_files=True,)
if images_uploaded is not None:
    st.image(images_uploaded)

if st.button("Create your ad"):
    if images_uploaded is not None:
        predictions = []
        for image in images_uploaded:
            img_tensor = load_image(image)
            prediction =  model.predict(img_tensor)
            predictions.append(class_names[np.argmax(prediction)])
        st.write(predictions)
    else:
        st.warning("Upload a photo before making predictions")
       
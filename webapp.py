import streamlit as st
from keras.models import load_model

# model = load_model(r"C:\Users\danie\Documentos\GitHub\RoomsClassifier\Models\model_transfer_learning\saved_model.pb")

st.title("Room Classifier")

image_uploaded = st.file_uploader("Upload your room image",type=["jpg","png"])
if image_uploaded is not None:
    st.image(image_uploaded)

if st.button("Predict"):
    if image_uploaded is not None:
       prediction =  model.predict(image_uploaded)
       st.write(prediction)
       
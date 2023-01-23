import streamlit as st
from keras.models import load_model
import tensorflow as tf
from keras.utils import load_img, img_to_array
import numpy as np
# Function to load the image in the format that the model can make the predictions and normalize it.
def load_image(img_path):

    img = load_img(img_path, target_size=(224, 224))
    img_tensor = img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.  

    return img_tensor

#Create a function to load the model of the classifier and store in the picle memory
# @st.experimental_singleton
# def load_model():
#     model = load_model('Models\model_transfer_learning\model_transfer_learning.h5')
#     return model
model = load_model('Models\model_transfer_learning\model_transfer_learning.h5')


# model = load_model(r"C:\Users\danie\Documentos\GitHub\RoomsClassifier\Models\model_transfer_learning\saved_model.pb")
#Load the model and the name of the classes
model = load_model('Models\model_transfer_learning\model_transfer_learning.h5')
class_names = ['Bathroom', 'Bedroom', 'House Map', 'Kitchen', 'Living Room']
#Create this varibale in case the add is create


# Create a sidebar menú
pages = st.sidebar.selectbox("Selecciona el menú", ["Create your ad", "Your ad"])
if pages == "Create your ad":
    #Create this variable in case the add is created
    add_created = False
    st.title("Place your real estate ad")
    
    operation = st.radio("Operation:",["Rent","Sale"])

    price = st.number_input("Price",min_value=0,step=50)

    city =  st.text_input("City")

    road_name =  st.text_input("Road name")

    description = st.text_area("Description: ",height=150, max_chars= 500)

    images_uploaded = st.file_uploader("Upload your Images here",type=["jpg","png","jpeg"],accept_multiple_files=True,)
    #If there is images show them
    if images_uploaded is not None:
        st.image(images_uploaded)
    #If all fields are fullfil create the add and make the predictions
    if st.button("Create your add or update it"):
        if images_uploaded is not None and price is not None and city is not None and road_name is not None and description is not None:
            add_created = True
            predictions = []
            for image in images_uploaded:
                img_tensor = load_image(image)
                prediction =  model.predict(img_tensor)
                predictions.append(class_names[np.argmax(prediction)])
            st.write(predictions)

            #Declare the variable in the session state to not lose after change to the other page
            st.session_state['operation'] = operation
            st.session_state['price'] = price
            st.session_state['city'] = city
            st.session_state['road_name'] = road_name
            st.session_state['description'] = description
            st.session_state['predictions'] = predictions
            st.session_state['images_upload'] = images_uploaded
            st.session_state['add_created'] = add_created
        else:
            st.warning("Fill in all the fields in order to create your advertisement.")

elif pages == "Your ad":
    if st.session_state['add_created']  == True:
        operation = st.session_state['operation']
        price = st.session_state['price'] 
        city = st.session_state['city']
        road_name = st.session_state['road_name']
        description = st.session_state['description'] 
        predictions = st.session_state['predictions'] 
        images_upload = st.session_state['images_upload']
        st.header(f"{operation} a real state in {city}, {road_name}")
        st.subheader(description)
    else:
        st.info("You should create the add first")
    


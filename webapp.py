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

def get_inputs(page):
    if page == "Create your ad":
        operation = st.radio("Operation:",["Rent","Sale"])

        price = st.number_input("Price",min_value=0,step=50)
        city =  st.text_input("City")
        road_name =  st.text_input("Road name")
        description = st.text_area("Description: ",height=150, max_chars= 500)
        images_uploaded = st.file_uploader("Upload your Images here",type=["jpg","png","jpeg"],accept_multiple_files=True,)
        if images_uploaded is not None:
            st.image(images_uploaded)

        if st.button("Create your add or update it"):
            if images_uploaded is not None and price is not None and city is not None and road_name is not None and description is not None:
                predictions = []
                for image in images_uploaded:
                    img_tensor = load_image(image)
                    prediction =  model.predict(img_tensor)
                    predictions.append(class_names[np.argmax(prediction)])
                st.write(predictions)
                return operation,price, city, road_name, description, images_uploaded, predictions
            else:
                st.warning("Fill in all the fields in order to create your advertisement.")

    elif page == "Your add":
        operation,price, city, road_name, description, images_uploaded, predictions = get_inputs("Create your app")
        return operation,price, city, road_name, description, images_uploaded, predictions


# model = load_model(r"C:\Users\danie\Documentos\GitHub\RoomsClassifier\Models\model_transfer_learning\saved_model.pb")
#Load the model and the name of the classes
model = load_model('Models\model_transfer_learning\model_transfer_learning.h5')
class_names = ['Bathroom', 'Bedroom', 'House Map', 'Kitchen', 'Living Room']
#Create this varibale in case the add is create
add_created = False

# Create a sidebar menú
pages = st.sidebar.selectbox("Selecciona el menú", ["Create your ad", "Your ad"])
if pages == "Create your ad":
    st.title("Place your real estate ad")

    get_inputs("Create your ad")
    
    # operation = st.radio("Operation:",["Rent","Sale"])

    # price = st.number_input("Price",min_value=0,step=50)

    # city =  st.text_input("City")

    # road_name =  st.text_input("Road name")

    # description = st.text_area("Description: ",height=150, max_chars= 500)

    # images_uploaded = st.file_uploader("Upload your Images here",type=["jpg","png","jpeg"],accept_multiple_files=True,)
    # if images_uploaded is not None:
    #     st.image(images_uploaded)

    # if st.button("Create your add or update it"):
    #     if images_uploaded is not None and price is not None and city is not None and road_name is not None and description is not None:
    #         add_created = True
    #         predictions = []
    #         for image in images_uploaded:
    #             img_tensor = load_image(image)
    #             prediction =  model.predict(img_tensor)
    #             predictions.append(class_names[np.argmax(prediction)])
    #         st.write(predictions)
    #     else:
    #         st.warning("Fill in all the fields in order to create your advertisement.")

else:
    get_inputs("Your add")
    st.info("Info")


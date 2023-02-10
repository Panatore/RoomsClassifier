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


#Load the model and the name of the classes
model = load_model('Models/vgg_model.h5')
class_names = ['Bathroom', 'Bedroom', 'House Map', 'Kitchen', 'Living Room']
#Create this variable in case the add is create


# Create a sidebar menú
pages = st.sidebar.selectbox("Selecciona el menú", ["Create your ad", "Your ad"])
if pages == "Create your ad":
    st.title("Place your real estate ad")
    #Check if the add is created
    if 'add_created' not in st.session_state:
        operation = st.radio("Operation:",["Rent","Sale"])

        price = st.number_input("Price",min_value=0,step=50)
        
        city =  st.text_input("City")

        road_name =  st.text_input("Road name")

        description = st.text_area("Description: ",height=150, max_chars= 500)

        num_bedrooms = st.number_input("Introduce the number of rooms",min_value=1,step=1)

        num_bathrooms = st.number_input("Introduce the number of bathrooms",min_value=1,step=1)

        surface_area = st.number_input("Surface area(m2): ",min_value=1,step=1)

        images_uploaded = st.file_uploader("Upload your Images here",type=["jpg","png","jpeg"],accept_multiple_files=True)
        #If there is images show them
        if images_uploaded is not None:
            st.image(images_uploaded)
    #If the add is created show the default the data saved and you have the option to change it
    else:
        if st.session_state['operation'] == 'Rent':
            operation = st.radio("Operation:",["Rent","Sale"],index=0)
        else:
            operation = st.radio("Operation:",["Rent","Sale"],index=1)

        price = st.number_input("Price",min_value=0,step=50,value = st.session_state['price'])

        city =  st.text_input("City",value= st.session_state['city'])

        road_name =  st.text_input("Road name",value= st.session_state['road_name'])

        description = st.text_area("Description: ",height=150, max_chars= 500, value= st.session_state['description'])

        num_bedrooms = st.number_input("Introduce the number of rooms",value= st.session_state['num_bedrooms'],min_value=1,step=1)

        num_bathrooms = st.number_input("Introduce the number of bathrooms",value= st.session_state['num_bathrooms'],min_value=1,step=1)

        surface_area = st.number_input("Surface area(m2): ",value= st.session_state['surface_area'],min_value=1,step=1)

        images_uploaded = st.file_uploader("Upload your Images here",type=["jpg","png","jpeg"],accept_multiple_files=True)
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
            #Declare the variable in the session state to not lose after change to the other page
            st.session_state['operation'] = operation
            st.session_state['price'] = price
            st.session_state['city'] = city
            st.session_state['road_name'] = road_name
            st.session_state['description'] = description
            st.session_state['predictions'] = predictions
            st.session_state['images_uploaded'] = images_uploaded
            st.session_state['num_bedrooms'] = num_bedrooms
            st.session_state['num_bathrooms'] = num_bathrooms
            st.session_state['surface_area'] = surface_area
            st.session_state['add_created'] = add_created
        else:
            st.warning("Fill in all the fields in order to create your advertisement.")

elif pages == "Your ad":
    if 'add_created' in st.session_state:
        st.sidebar.write('This is your real state add')
        operation = st.session_state['operation']
        price = st.session_state['price'] 
        city = st.session_state['city']
        road_name = st.session_state['road_name']
        description = st.session_state['description'] 
        predictions = st.session_state['predictions'] 
        images_uploaded = st.session_state['images_uploaded']
        num_bedrooms = st.session_state['num_bedrooms']
        num_bathrooms = st.session_state['num_bathrooms']
        surface_area = st.session_state['surface_area']
        st.header(f"{operation} a real state in {city}, {road_name}")
        st.subheader(f"Price: {price} €")
        #Get the indexes of each class predictions
        bathroom_idx = [index for (index, item) in enumerate(predictions) if item == "Bathroom"]
        bedroom_idx = [index for (index, item) in enumerate(predictions) if item == "Bedroom"]
        housemap_idx = [index for (index, item) in enumerate(predictions) if item == "House Map"]
        kitchen_idx = [index for (index, item) in enumerate(predictions) if item == "Kitchen"]
        livingroom_idx = [index for (index, item) in enumerate(predictions) if item == "Living Room"]
        BathroomTab, BedroomTab, HouseMapTab, KitchenTab, LivingRoomTab = st.tabs(class_names)
        with BathroomTab:
            if bathroom_idx:
                for index in bathroom_idx:
                    st.image(images_uploaded[index],use_column_width='always')
            else:
                st.write("There is no image of the Bathroom")
        with BedroomTab:
            if bedroom_idx:
                for index in bedroom_idx:
                    st.image(images_uploaded[index],use_column_width='always')
            else:
                st.write("There is no images of the Bedroom")
        with HouseMapTab:
            if housemap_idx:
                for index in housemap_idx:
                    st.image(images_uploaded[index],use_column_width='always')
            else:
                st.write("There is no images of the House Map")   
        with KitchenTab:
            if kitchen_idx:
                for index in kitchen_idx:
                    st.image(images_uploaded[index],use_column_width='always')
            else:
                st.write("There is no images of the Kitchen")
        with LivingRoomTab:
            if livingroom_idx:
                for index in livingroom_idx:
                    st.image(images_uploaded[index],use_column_width='always')
            else:
                st.write("There is no images of the Living Room")
        st.subheader("Description:")
        st.write(description)
        st.subheader(f"Nº of bedrooms: {num_bedrooms}")
        st.subheader(f"Nº of bathrooms: {num_bathrooms}")
        st.subheader(f"Surface area: {surface_area}m2")
    else:
        st.info("You should create the add first")
    


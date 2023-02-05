from flask import Flask, render_template, request
from keras.models import load_model
from keras.utils import load_img, img_to_array
import numpy as np
import tensorflow as tf
import os

model = load_model('model_transfer_learning.h5')
#Create the app
app = Flask(__name__)

def load_image(img_path):


    img = load_img(img_path, target_size=(224, 224))
    img_tensor = img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.  

    return img_tensor

def clasificar_fotos(images):
  # código para cargar tu modelo de TensorFlow y usarlo para clasificar las fotos
  # (debes reemplazar esto por tu propio código)
  class_names = ['Bathroom', 'Bedroom', 'House Map', 'Kitchen', 'Living Room']
  clasificaciones = []
  for image in images:
    img_tensor = load_image(image)
    prediction = model.predict(img_tensor)
    clasificaciones.append(class_names[np.argmax(prediction)])
  return clasificaciones

@app.route('/')
def home():
  # aquí podrías obtener los anuncios de tu base de datos o de donde los almacenes
    #anuncios = obtener_anuncios()
  return render_template('home.html')

# def guardar_fotos(fotos):
#   # código para guardar la foto en algún lugar (por ejemplo, en una carpeta del servidor o en un servicio de almacenamiento en la nube)
#   # (debes reemplazar esto por tu propio código)
#   nombre = fotos.filename
#   ruta = os.path.join('static/fotos', nombre)
#   fotos.save(ruta)
#   return ruta

@app.route('/crear_anuncio', methods=['GET', 'POST'])
def crear_anuncio():
  if request.method == 'POST':
    # recoge los datos del formulario
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    fotos = request.files.getlist('foto')

    predictions = clasificar_fotos(fotos)

    # crea un diccionario con los datos del anuncio
    anuncio = {'titulo': titulo, 'descripcion': descripcion, 'precio': precio, "fotos": fotos, 'predictions': predictions}
    print(anuncio)
    # guarda el anuncio y las fotos en la base de datos
    # redirige al usuario a la página principal
    return "Hola Mundo"
  else:
    # muestra el formulario para crear el anuncio
    return render_template('create.html')


if __name__ == '__main__':
  app.run()

from keras.applications import MobileNetV2, VGG16, ResNet101V2, InceptionV3
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D
from keras.optimizers import SGD, Adam
from keras.models import Model

data_dir = "./data/Train/"
width_shape = 224
height_shape = 224
num_classes = 5
epochs = 50
batch_size = 32 

# Cargar el modelo preentrenado
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224,224,3))

# Congelar las capas del modelo
for layer in base_model.layers:
  layer.trainable = False

# Añadir una capa completamente conectada al final
x = base_model.output
x=GlobalAveragePooling2D()(x)
x=Dense(1024,activation='relu')(x) #we add dense layers so that the model can learn more complex functions and classify for better results.
x=Dense(1024,activation='relu')(x) #dense layer 2
x=Dense(512,activation='relu')(x) #dense layer 3
x = Dropout(0.5)(x)
# x = base_model.output
# x = Flatten()(x)
# x = Dense(1024, activation='relu')(x)
# x = Dropout(0.5)(x)
predictions=Dense(num_classes,activation='softmax')(x) #final layer with softmax activation

# Crear un modelo basado en el modelo preentrenado
model = Model(inputs=base_model.input, outputs=predictions)

# Compilar el modelo
model.compile(optimizer=SGD(lr=0.001, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])

# Preparar los datos de entrenamiento y validación
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   validation_split=0.2)

valid_datagen = ImageDataGenerator(rescale=1./255, validation_split= 0.2)


train_generator = train_datagen.flow_from_directory(data_dir,
    target_size=(width_shape, height_shape),
    color_mode="rgb",
    class_mode='categorical',
    subset= "training",
    batch_size= batch_size)

validation_generator = valid_datagen.flow_from_directory(data_dir,
    target_size=(width_shape, height_shape),
    color_mode="rgb",
    class_mode='categorical',
    subset= "validation",
    batch_size= batch_size)


# Entrenar el modelo
history = model.fit(
      train_generator,
      steps_per_epoch=train_generator.samples/train_generator.batch_size ,
      epochs=15,
      validation_data=validation_generator,
      validation_steps=validation_generator.samples/validation_generator.batch_size,
      verbose=1)

# Descongelar todas las capas del modelo
for layer in base_model.layers:
  layer.trainable = True

# Compilar el modelo con un learning rate bajo
model.compile(optimizer=SGD(lr=0.0001, momentum= 0.9), loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(
      train_generator,
      steps_per_epoch=train_generator.samples/train_generator.batch_size ,
      epochs=15,
      validation_data=validation_generator,
      validation_steps=validation_generator.samples/validation_generator.batch_size,
      verbose=1)

# Guardar el modelo entrenado
model.save('fine_tuned_model.h5')
model.evaluate_generator()

#Con SGD 0btengo 0.8892 de accuracy (lr=0.0001, momentum=0.9) en el fine tuning y SGD(lr=0.001, momentum=0.9) en el transfer learning
#Con Adam obtengo 0.9002 con un learning rate = 0.0005 en el fine tuning
#Voy a cambiar las capas que añado para ver si hay mejoría(Estas son las que tengo) 
# x = base_model.output
# x = Flatten()(x)
# x = Dense(1024, activation='relu')(x)
# x = Dropout(0.5)(x)
# predictions = Dense(num_classes, activation='softmax')(x)
# Con la configuración misma que el notebook de TFM el fine tuning no tiene mejoría 0.76 de accuracy con Adam y con SGD 0.87
#Voy a aumentar la epochs a 15 tenemos 0.9015 con SGD con MobilnetV2
#Con VGG16 obtenemos 0.9126
#Con INceptionV3 tenemos  0.9
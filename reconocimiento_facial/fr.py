# importación de las librerías
import os
import face_recognition

# Se genera una lista de todas las imágenes disponibles
images = os.listdir('images')

# Se “carga” la imagen a revisar
image_to_be_matched = face_recognition.load_image_file('palmer_chelsea.jpeg')

# Se codifica la imagen cargada en el vector de características
image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]

# Se realizan las iteraciones con cada imagen que se tiene almacenada “corpus”
for image in images:
    # se “carga” la imagen
    current_image = face_recognition.load_image_file("images/" + image)
    # se codifica la imagen en el vector de características
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    # se revisa la imagen cargada con cada imagen del corpus
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
    # se determinar si la imagen se encontró o no
    if result[0] == True:
        print ("Se encontró la imagen: " + image)
    else:
        print ("No existe la imagen: " + image)
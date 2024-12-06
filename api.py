from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from keras.models import load_model

# Initialiser l'application FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working!"}

# Charger le modèle et définir les classes
model = load_model('dog_breed.h5')
CLASS_NAMES = ['scottish_deerhound', 'maltese_dog', 'bernese_mountain_dog', 'entlebucher']

   
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint pour prédire la race de chien.
    Accepte une image au format JPG.
    """
    try:
        # Lire l'image envoyée
        file_bytes = await file.read()
        np_array = np.frombuffer(file_bytes, np.uint8)
        opencv_image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        # Redimensionner l'image
        resized_image = cv2.resize(opencv_image, (224, 224))
        resized_image = resized_image.reshape((1, 224, 224, 3))

        # Prédiction
        prediction = model.predict(resized_image)
        predicted_class = CLASS_NAMES[np.argmax(prediction)]

        # Retourner le résultat
        return JSONResponse(content={"breed": predicted_class})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


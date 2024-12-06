from fastapi import FastAPI
from fastapi.responses import JSONResponse
import numpy as np
from keras.models import load_model

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

model = load_model('dog_breed.h5')
@app.post("/predict")
async def predict():
    """
    Endpoint pour prédire la race de chien.
    Accepte une image au format JPG.
    """
    try:
        # Retourner le résultat
        return JSONResponse(content={"breed": "maltese dog"})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


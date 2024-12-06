from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
from keras.models import load_model

# Initialiser l'application FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working!"}

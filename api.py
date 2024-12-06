from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint pour prédire la race de chien.
    Accepte une image au format JPG.
    """
    try:
        # Retourner le résultat
        return JSONResponse(content={"breed": "maltese dog"})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


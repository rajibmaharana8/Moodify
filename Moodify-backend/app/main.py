from fastapi import FastAPI, UploadFile, File
from app.emotion_model import predict_emotion

app = FastAPI(title="Moodify Backend API")

@app.get("/")
def root():
    return {"message": "Moodify backend running"}

@app.post("/predict-emotion")
async def predict_emotion_api(file: UploadFile = File(...)):
    image_bytes = await file.read()
    emotion = predict_emotion(image_bytes)
    return {
        "emotion": emotion
    }
import cv2
import numpy as np
from tensorflow.keras.models import load_model

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "emotion_model.h5")

model = load_model(MODEL_PATH)

EMOTIONS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

def predict_emotion(image_bytes):
    # Convert bytes to OpenCV image
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    if img is None:
        return "neutral"

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(gray, (48, 48))

    face = face / 255.0
    face = face.reshape(1, 48, 48, 1)

    preds = model.predict(face)
    emotion = EMOTIONS[np.argmax(preds)]

    return emotion

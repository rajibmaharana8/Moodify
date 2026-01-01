from emotion_model import predict_emotion

with open("Screenshot 2026-01-02 042350.png", "rb") as f:
    img_bytes = f.read()

print(predict_emotion(img_bytes))
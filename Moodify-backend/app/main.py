from fastapi import FastAPI

app = FastAPI(title="Moodify Backend API")

@app.get("/")
def root():
    return {"message": "Moodify backend is running successfully"}
    
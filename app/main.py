from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from model.model import predict_pipeline
from model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check here": "OK", "model_version": model_version}


@app.get("/test")
def testFunction():
    return {"test message": "hello hunyy bunny"}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language":language}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")

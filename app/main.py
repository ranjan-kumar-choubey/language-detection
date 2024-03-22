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

# uncomment only for development , not for production
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")


# sudo docker ps -a
# sudo docker build -t language-detection-app .
# sudo docker run -d --name test-add -p 80:80 language-detection-app
# sudo docker rm <container_id>

#sudo lsof -i -P -n | grep 8080
#sudo kill -9 <portno>      ,or 
# kill -9 $(lsof -t -i tcp:<port#>)
# docker exec -it <container_id> bash //to enter into docker 
# commnet

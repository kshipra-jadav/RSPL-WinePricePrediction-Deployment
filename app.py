from predict import start
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Values(BaseModel):
    winery: str
    wine: str
    rating: float
    region: str
    body: float

@app.get('/')
def hello():
    return {"hello": "world"}

@app.post('/predict')
def predict(value: Values):
    price = start(value.winery, value.wine, value.rating, value.region, value.body)
    return(f"The predicted price is :- {price[0]}")


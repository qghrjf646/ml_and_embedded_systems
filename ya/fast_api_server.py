from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class HouseFeatures(BaseModel):
    size: float
    n_bedrooms: int
    has_garden: int

model = joblib.load("regression.joblib")

@app.post("/predict")
def predict(features: HouseFeatures):
    result = model.predict([[features.size, features.n_bedrooms, features.has_garden]])[0]
    return {"predicted_price": result}
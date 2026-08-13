import pickle
import uvicorn
from fastapi import FastAPI
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra="forbid")
    lead_source: Literal["organic_search", "social_media", "paid_ads", "referral", "events"]
    number_of_courses_viewed: int = Field(..., ge=0)  
    annual_income: float = Field(..., ge=0.0)

class ConvertPredictResponse(BaseModel):
    convert_probability: float = Field(..., ge=0.0, le=1.0)
    convert: bool

app = FastAPI(title="user-convert-prediction")

with open('pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(user):
    score = pipeline.predict_proba(user)[0, 1]
    return float(score)

@app.post("/predict")
def predict(user: User) -> ConvertPredictResponse:
    convert_prob = predict_single(user.model_dump()) 
    return ConvertPredictResponse(
        convert_probability=convert_prob,
        convert=bool(convert_prob >= 0.5)
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

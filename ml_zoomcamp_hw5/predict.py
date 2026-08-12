import pickle
import uvicorn
from fastapi import FastAPI
from typing import Dict, Any


app = FastAPI(title="user-convert-prediction")

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(user):
    score = pipeline.predict_proba(user)[0, 1]
    return float(score)

@app.post("/predict")
def predict(user: Dict[str, Any]):
    convert_prob = predict_single(user) 
    return {
        "convert_probability": convert_prob,
        "convert": bool(convert_prob >= 0.5)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

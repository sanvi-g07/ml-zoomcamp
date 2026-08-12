import pickle


with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

user = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

def predict_single(user):
    score = pipeline.predict_proba(user)[0, 1]
    return float(score)

def predict(user):
    convert_prob = predict_single(user) 
    return {
        "convert_probability": convert_prob,
        "convert": bool(convert_prob >= 0.5)
    }

result = predict(user)
print(result)

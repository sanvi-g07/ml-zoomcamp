import requests

url = "http://127.0.0.1:8080/predict"

user = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

response = requests.post(url, json=user)
result = response.json()

print("Convert Probability: ", result['convert_probability'])
print("Convert: ", result['convert'])

# Question 4
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
print(requests.post(url, json=client).json())
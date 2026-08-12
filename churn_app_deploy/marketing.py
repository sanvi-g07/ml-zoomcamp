import requests

url = 'http://localhost:8080/predict'
#url = "https://lively-beacon-1052.fly.dev/predict"

customer = {
    "gender": "male",
    "seniorcitizen": 0,
    "partner": "no",
    "dependents": "yes",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 6,
    "monthlycharges": 29.85,
    "totalcharges": 129.85
}

response = requests.post(url, json=customer)
churn = response.json()

print("response: ", churn)
print("prob of churning: ", churn['churn_probability'])

if churn['churn'] >= 0.5:
    print("send email with promo")
else:
    print("don't do anything")
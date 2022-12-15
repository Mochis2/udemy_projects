import requests
from datetime import datetime
import os

#is on replit

APP_ID = "Nutritionix"
API_KEY = "Nutritionix"
TOKEN = "Bearer sheety"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

input_query = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_parameters = {
    "query": input_query,
    "gender": "male",
    "weight_kg": 68,
    "height_cm": 185,
    "age": 20
}

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_parameters)
data = response.json()

sheety_endpoint = "sheety"

today = datetime.now()

for dict in data["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": dict["name"].title(),
            "duration": dict["duration_min"],
            "calories": dict["nf_calories"]
        }
    }
    headers1 = {
        "Authorization": TOKEN
    }
    response1 = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=headers1)
print(response1.text)
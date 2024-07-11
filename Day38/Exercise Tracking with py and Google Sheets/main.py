import requests
import datetime as dt
import os

APP_ID = "ad03736d"
API_KEY = os.environ["APP_ID"]

WEIGHT_KG = 45
HEIGHT_CM = 160
AGE = 21
GENDER = "female"


user_text = input("Tell me which Exercise you did? ")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


api_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": user_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE,
}

response = requests.post(url=nutrition_endpoint, json=parameters, headers=api_headers)
data = response.json()["exercises"]
print(data)

sheety_endpoint = "https://api.sheety.co/c833c61645ee58aa81912af54c1c816c/workoutTracking/workouts"

today_date = dt.datetime.now().strftime("%d/%m/%Y")
today_time = dt.datetime.now().strftime("%H:%M:%S")

sheety_header=(
    "sharyuadsul19",
    "Adsul@12345"
)

for exercise in data:
    sheety_parameters={
        "workout":{
            "date": today_date,
            "time": today_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_parameters, auth=sheety_header)
    print(response.text)



#get the help of  https://sheety.co/docs/requests  doc


# response = requests.get(sheety_endpoint)
# print(response.json())

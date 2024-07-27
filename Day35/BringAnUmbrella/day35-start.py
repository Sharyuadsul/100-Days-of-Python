import requests
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='../../.env')
from twilio.rest import Client


owm_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
aplikey= os.environ["WEATHER_APIKEY"]

account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

parameters = {
    "lat":18.520430,
    "lon":73.856743,
    "appid":aplikey,
    "cnt":4,
}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()

will_rain = False
weather_data=response.json()
# print(weather_data)
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code<850:    #it should be <700 for the rain
        will_rain=True

if will_rain:
    print("Bring An Umbrella!")
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        body="Its going to rain today. Bring an Umbrella..",
        from_=os.getenv('TWILIO_NUMBER'),
        to=os.getenv('MY_NUMBER')
    )
    print(message.status)




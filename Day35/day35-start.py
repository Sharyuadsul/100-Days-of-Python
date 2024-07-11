import requests
# from twilio.rest import Client


owm_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
aplikey= "c325125cc8d0e6501bb539b60e04b700"

# account_sid = 'AC367c2f48d34f2c56c893d9532ac25ef5'
# auth_token = '[AuthToken]'

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
    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #         .create(
    #     body="Its going to rain today. Bring an Umbrella..",
    #     from_='+13345818652',
    #     to='Your verified number'
    # )
    # print(message.status)




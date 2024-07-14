import requests
import datetime as dt
import smtplib
import time
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')
from twilio.rest import Client

MY_LAT= 18.520430
MY_LNG=73.856743

my_mail="sharyuadsul19@gmail.com"
password = os.getenv('APP_PASSWORD')

def is_issoverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    # iss_position = (latitude,longitude)

    #your position is within +5 or -5 degrees os ISS position
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True


def is_night():
    parameters ={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    print(sunrise)
    print(sunset)

    now = dt.datetime.now()
    if sunset <= now.hour <=sunrise:
        return True

while True:
    time.sleep(60)
    if is_issoverhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(user=my_mail, password=password)
            conn.sendmail(from_addr=my_mail,
                          to_addrs=my_mail,
                          msg="Subject: ISS Overhead\n\nLook Up!!\nThe ISS is above your head in the sky")



#if ISS is close to my current location
#if s currently dark
#then send me an email to look up
#run code every 60 seconds
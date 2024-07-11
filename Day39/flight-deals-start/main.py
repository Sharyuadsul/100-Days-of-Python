#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint

API_KEY = "ZBMY8OsdCOIV4MNyniJwaC3JVc5irbOE"
API_SECRET = "kvnwwBpCrvFf3llv"

bas_url = "test.api.amadeus.com"
sheety_url = "https://api.sheety.co/c833c61645ee58aa81912af54c1c816c/flightDeals/prices"

response = requests.get(url =sheety_url)
sheet_data = response.json()["prices"]

for item in sheet_data:
    if item["iataCode"] ==


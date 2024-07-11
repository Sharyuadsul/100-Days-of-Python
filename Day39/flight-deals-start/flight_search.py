import requests

sheety_url = "https://api.sheety.co/c833c61645ee58aa81912af54c1c816c/flightDeals/prices"
parameters = {
    "prices":{
        "iataCode":"TESTING"
    }
}

class FlightSearch(data):
    for item in data:
        if item["iataCode"] == "":
            requests.post(url = sheety_url, json=parameters)
    #This class is responsible for talking to the Flight Search API.
    pass
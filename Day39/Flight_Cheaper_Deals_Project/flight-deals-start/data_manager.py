# This class is responsible for talking to the Google Sheet.

from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='../../../.env')
import requests
# from pprint import pprint


# load_dotenv()
# sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
SHEETY_USERNAME = os.getenv('SHEETY_USERNAME')
SHEETY_PASSWORD = os.getenv('SHEETY_PASSWORD')
SHEETY_ENDPOINT = "https://api.sheety.co/c833c61645ee58aa81912af54c1c816c/flightDeals/prices"
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
headers = {
    "Authorization": f"Basic {SHEETY_TOKEN}"
}

class DataManager:
    def __init__(self):
        # self.user = os.environ["SHEETY_USERNAME"]
        # self.password =os.environ["SHEETY_PASSWORD"]
        self.destination_data = {}


    def get_sheet_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=headers)
        data= response.json()
        # print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city['iataCode']
                }
            }

            response = requests.put(f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
            # print(response.text)

#
# obj = DataManager()
# obj.get_sheet_data()
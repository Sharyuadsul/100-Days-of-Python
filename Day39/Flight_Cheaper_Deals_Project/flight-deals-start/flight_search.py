# This class is responsible for talking to the Flight Search API.
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='../../../.env')

import requests
from datetime import datetime

from datetime import datetime, timedelta
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    def __init__(self):
        self.api_key=AMADEUS_API_KEY
        self.api_secret=AMADEUS_API_SECRET
        self.token = self.get_new_token()
    def get_iataCode(self, city_name):
        """
        Retrieves the IATA code for a specified city using the Amadeus Location API.
        Parameters:
        city_name (str): The name of the city for which to find the IATA code.
        Returns:
        str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError,
        or "Not Found" if no match is found due to a KeyError.

        """

        print(f"using {self.token} this token to get the destination code")
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(IATA_ENDPOINT, headers=header, params=query)
        # print(response.json())

        print(f"Status code {response.status_code}. Airport IATA: {response.json()["data"][0]}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def get_new_token(self):
        #To make any requests to Amadeus, we first need a token (the Amadeus API key and Secret is not sufficient).
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': AMADEUS_API_KEY,
            'client_secret': AMADEUS_API_SECRET
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # print(response.json())

        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "Authorization":f"Bearer {self.token}"
        }
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode":"GBP",
            "max":"10",
        }

        response = requests.get(FLIGHT_ENDPOINT, headers=headers, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n")
            print(response.text)
            return None

        return response.json()


# obj = FlightSearch()
#
# data = obj.check_flight("LON", "PAR", tomorrow, six_month_from_today)
# print(data)
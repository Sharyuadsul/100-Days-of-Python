#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import time
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import get_cheapest_flight
from notification_manager import NotificationManager


datamanager = DataManager()
sheet_data = datamanager.get_sheet_data()
flightsearch = FlightSearch()
notificationmanager = NotificationManager()


for city in sheet_data:
    if city['iataCode'] == "":
        city['iataCode'] = flightsearch.get_iataCode(city['city'])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"Sheet Data:\n{sheet_data}")

datamanager.destination_data = sheet_data
datamanager.update_iata()

ORIGIN_CITY = "LON"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for city in sheet_data:
    print(f"Getting flights for {city['city']}...")
    flights = flightsearch.check_flight(origin_city_code=ORIGIN_CITY,
                                        destination_city_code=city['iataCode'],
                                        from_time = tomorrow,
                                        to_time=six_month_from_today)

    cheapest_flight= get_cheapest_flight(data=flights)
    # print(f"{city['city']}: £{cheapest_flight.price}")
    if cheapest_flight.price != "N/A" and cheapest_flight.price < city["lowestPrice"]:
        print(f"Lower price flight found to {city['city']}!")
        notificationmanager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_city_code} to {cheapest_flight.destination_city_code}, "
                         f"on {cheapest_flight.from_date} until {cheapest_flight.to_date}.")
        # notificationmanager.send_whatsapp(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_city_code} to {cheapest_flight.destination_city_code}, "
        #                  f"on {cheapest_flight.from_date} until {cheapest_flight.to_date}.")




    # Slowing down requests to avoid rate limit
    time.sleep(2)






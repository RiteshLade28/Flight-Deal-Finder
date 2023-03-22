#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_details import User_Details
import sys

# user_details = User_Details()
# user_details.add_user()

data_manager = DataManager()
# sheet_data = data_manager.get_destination_data()
sheet_data = data_manager.dump_spreadsheet()
# print(sheet_data)

TOMORROW = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime(f"%d/%m/%Y")
DAY_AFTER_SIX_MONTHS = (datetime.datetime.now() + datetime.timedelta(days=6 * 30)).strftime(f"%d/%m/%Y")
RETURN_FROM = (datetime.datetime.now() + datetime.timedelta(days=6 * 30 + 7)).strftime(f"%d/%m/%Y")
RETURN_TO = (datetime.datetime.now() + datetime.timedelta(days=6 * 30 + 30)).strftime(f"%d/%m/%Y")
FLY_FROM = "DEL"

flight_search = FlightSearch()
if sheet_data[0]["iataCode"] == "":

    for city in sheet_data:
        city["iataCode"] = flight_search.get_destination_code(city["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for city in sheet_data:
    # print(city["iataCode"])
    flight = flight_search.search_for_flights(
        fly_from=FLY_FROM,
        fly_to=city["iataCode"],
        date_from=TOMORROW,
        date_to=DAY_AFTER_SIX_MONTHS,
        return_from=RETURN_FROM,
        return_to=RETURN_TO,
    )

    if flight is not None and flight.price < city["lowestPrice"]:
        print("low price")
        notification_manager = NotificationManager()
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        notification_manager.send_emails(message, link)


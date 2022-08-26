#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

dataManager = DataManager()
sheet_data = dataManager.get_destination_data()

if sheet_data[0]["iataCode"]=="":
    from flight_search import FlightSearch
    flightSearch = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flightSearch.get_destination_code(row["city"])
        print(sheet_data)
        dataManager.destination_data = sheet_data
        dataManager.update_destination_codes()
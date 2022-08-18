# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from pprint import pprint
import requests
sheet_endpoint_get = "https://api.sheety.co/bcdd9bd4849a93ee3ffa8d8df8c6acce/flightDeas/sheet1"
flight_search_api = "https://tequila-api.kiwi.com/locations/query"
flight_header = {
    "apikey": "Z552Orcb6XRi_8fFyVvrISbQXLY85OBk"
}

sheety_get_response = requests.get(url=sheet_endpoint_get)
sheety_get_response_dict = sheety_get_response.json()
pprint(sheety_get_response_dict)
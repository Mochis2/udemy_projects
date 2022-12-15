import requests
from datetime import datetime, timedelta
from notification_manager import NotificationManager


TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "https://tequila.kiwi.com/portal/my-solutions" #on there
IATA_CODE_LIST = ["PAR","BER","TYO","SYD","IST","KUL","NYC","SFO","CPT","LON"]

class FlightSearch:
    
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.teq_header = {
            "apikey": TEQUILA_API_KEY
        }
        self.today = datetime.now().strftime("%d/%m/%Y")
        self.in_six_months = (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y")


    def get_destination_code(self, city_name):
        teq_params = {
            "term": city_name,
            "location_types": "city",
            "locale": "en-US"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=teq_params, headers=self.teq_header)
        data = response.json()
        # print(data)
        code = data["locations"][0]["code"]
        return code


    def get_flight_info(self):
        noti = NotificationManager()
        for iata in IATA_CODE_LIST:
            flight_params = {
                "fly_from": "ZRH",
                "fly_to": iata,
                "date_from": self.today,
                "date_to": self.in_six_months,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "ret_to_diff_city": False,
                "ret_from_diff_city": False,
                "curr": "CHF",
                "max_stopovers": 2,
                "limit": 1,
                "max_fly_duration": 40
            }
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=flight_params, headers=self.teq_header)
            data = response.json()
            price = data["data"][0]["price"]
            city_to = data["data"][0]["cityTo"]
            d_time = data["data"][0]["route"][0]["dTime"]
            stop_over_1 = data['data'][0]['route'][0]['cityTo']
            stop_over_2 = data['data'][0]['route'][1]['cityTo']
            link_to_flight = data['data'][0]['deep_link']
            departure = datetime.fromtimestamp(d_time)
            print(f"\n{city_to}: {price} CHF | Departure at: {departure.strftime('%d-%m-%Y %X')}.")
            if stop_over_1 != city_to:
                print(f"This Flight has a stop over, via: {stop_over_1}")
            elif stop_over_1 != city_to and stop_over_2 != city_to:
                print(f"This Flight has a stop over, via: {stop_over_1} and {stop_over_2}")
            print(f"\nHere is the link: {link_to_flight}")
            noti.send_email()
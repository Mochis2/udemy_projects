import requests
from twilio.rest import Client
api_key = "psst🤫"
account_sid = "ACa1c25d5dcf3068565809bd9f1ad6c1a3"
auth_token = "psst"
# lat = 47.519981
# long = 8.935250

lat = 40.426667
long = -3.700667


parameters = {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    "units": "metric",
    "cnt": 5
}


response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
list_data = weather_data["list"]

weather_id_list = [list_data[i]["weather"][0]["id"] for i in range(0,4)]
will_rain = any(id in weather_id_list for id in weather_id_list if id < 700)

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It's goin to rain today LETSGOOOOO 🌧️",
                     from_='+19362275601',
                     to='+41788478989'
                 )

print(message.status)

# if using pythonanywhere: https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.499882 # Your latitude
MY_LONG = 8.726160 # Your longitude

MY_EMAIL = "morriseberhard11@gmail.com"
PASSWORD = "prdchsnhtadbmopo"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


def check_if_iss_is_near():
    if iss_latitude <= MY_LAT+5 and iss_latitude >= MY_LAT-5 and iss_longitude <= MY_LONG+5 and iss_longitude >= MY_LONG-5:
        return True
    else: return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

def check_if_dark():
    if time_now >= sunset or time_now <= sunrise:
        return True
    else: return False

while True:
    time.sleep(60)
    if check_if_iss_is_near() and check_if_dark():

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="morriseberhard44@gmail.com", msg="Subject:YO LOOK UP THE ISS IS IN THE SKY\n\nI HOPE IT ISN'T CLOUDY")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




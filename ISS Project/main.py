import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "auscultarem@gmail.com"
MY_PASSWORD = "12345"
MY_LAT = 20.659698
MY_LONG = -103.349609

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    min_lat = MY_LAT - 5
    max_lat = MY_LAT + 5
    min_long = MY_LONG - 5
    max_long = MY_LONG + 5

    if (min_lat <= iss_latitude <= max_lat) and (min_long <= iss_longitude <= max_long):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # sunrise = sunrise.split("T")
    # sunset = sunset.split("T")
    # print(sunrise.split("T")[1].split(":")[0]) # to get the hour

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up\n\nThe ISS is above you in the sky."
        )
import requests
from datetime import datetime
import smtplib
import time

# This program uses APIs to get the international space station's location 
# and your own location and sends you an email when the ISS is visible from your location

MY_LAT = "your latitud" ## DATA NEEDED
MY_LONG = "your longitude" ## DATA NEEDED
my_email = "123@dominio.com"
my_password = "password"


def is_ISS_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT-5) < iss_latitude < (MY_LAT+5) and (MY_LONG-5) < iss_longitude < (MY_LONG+5):
        return True


def is_night():
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
    time_now = datetime.now()
    if sunset < time_now.hour or time_now.hour < sunrise:
        return True


def send_mail():
    if is_ISS_overhead and is_night:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="subject:ISS location\n\n Look up!!, it's over your head!!"
                )
            time.slepp(60)
            send_mail()

send_mail()

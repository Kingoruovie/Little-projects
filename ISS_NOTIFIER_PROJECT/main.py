import requests
import datetime as dt
import smtplib
import time

MY_LAT = 6.334250
MY_LONG = 5.614090
MY_MAIL = "pythontrialovie@yahoo.com"
PASSWORD = "qenkdyfnvjrvixkg"

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_latitude = float(iss_response.json()["iss_position"]["latitude"])
iss_longitude = float(iss_response.json()["iss_position"]["longitude"])


parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

now = dt.datetime.now()


def check_position_iss():
    if (MY_LAT - 3 < iss_latitude < MY_LAT + 3) and (MY_LONG - 3 < iss_longitude < MY_LONG + 3)\
            and (now.hour >= sunset or now.hour <= sunrise):
        return True


while True:
    time.delay(60)
    if check_position_iss():
        with smtplib.SMTP("smtp.mail.yahoo.com") as message:
            message.starttls()
            message.login(user=MY_MAIL, password=PASSWORD)
            message.sendmail(
                from_addr=MY_MAIL,
                to_addrs="oruovie@gmail.com",
                msg="Subject:ISS NOTIFICATION\n\nLook up!!!The ISS is over your head🤗🤗🤗🤗".encode("utf-8")
            )

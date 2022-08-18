import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

with open("./quotes.txt", encoding="utf-8") as data_file:
    data = data_file.readlines()
    stripped_data = []
    for item in data:
        stripped_data.append(item.strip())
    print(stripped_data)
my_email = "pythontrialovie@yahoo.com"
password = "spczfmxoarsfbxgm"

random_quote = random.choice(stripped_data)

with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
    connection.login(user=my_email, password=password)
    if day_of_week == 3:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pythontrialg@gmail.com",
            msg=f"Subject:Quote of the day\n\n{random_quote}".encode("utf-8")
        )

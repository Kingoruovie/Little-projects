import smtplib
import datetime as dt
import random
import pandas

MY_MAIL = "pythontrialg@gmail.com"
PASSWORD = "abcd123456()"
items = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
letters = []


def convert_letter(letter):
    with open(letter, encoding="utf-8") as data_file:
        data = data_file.readlines()
        letters.append(data)


for item in items:
    convert_letter(item)

people_details = pandas.read_csv("./birthdays.csv")
people_details_list = people_details.to_dict(orient="records")
print(people_details_list)

now = dt.datetime.now()

for people in people_details_list:
    if people["month"] == now.month and people["day"] == now.day:
        with smtplib.SMTP_SSL("smtp.gmail.com") as birthday_mail:
            birthday_mail.login(user=MY_MAIL, password=PASSWORD)
            letter_planned = random.choice(letters)
            new_letter_in_string = "".join(letter_planned)
            letter_to_send = new_letter_in_string.replace("[NAME]", people['name'])
            birthday_mail.sendmail(
                from_addr=MY_MAIL,
                to_addrs=people["email"],
                msg=f"Subject:HAPPY BIRTHDAY\n\n{letter_to_send}".encode("utf-8")
            )

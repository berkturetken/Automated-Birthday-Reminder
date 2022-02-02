# ---------- Automated Birthday Reminder (ABR) ----------
import datetime as dt
import pandas
import smtplib
from dotenv import load_dotenv
import os

# CONSTANTS
local_key_path = "C:/Programming/Keys/key.txt"
load_dotenv(local_key_path)

MY_EMAIL = os.getenv("berkturetken1_gmail")
PWD = os.getenv("berkturetken1_pwd")
RECEIVER_EMAIL = "berkturetken@sabanciuniv.edu"
RECEIVER_EMAIL_2 = "buket.karakas@aalto.fi"
RECEIVER_EMAIL_3 = "gokktugbasaran@gmail.com"

# Read the csv file
data = pandas.read_csv("docs/birthdays.csv")
people_birthday_dates = data.to_dict(orient="records")

# Get the current month and day
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# Check whether today is someone's birthday
for person in people_birthday_dates:
    if current_month == person["month"] and current_day == person["day"]:
        print(person)
        file_path = "docs/letter.txt"

        # Prepare the notification for email
        with open(file_path) as file:
            text = file.read()
            letter_final_version = text.replace("[NAME]", person["name"])

        # Send the letter to the specified email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PWD)
            # Send to me
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Birthday Reminder!\n\n{letter_final_version}"
            )
            # Send to Buket
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVER_EMAIL_2,
                msg=f"Subject:Birthday Reminder!\n\n{letter_final_version}"
            )
            # Send to Göktuğ
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVER_EMAIL_3,
                msg=f"Subject:Birthday Reminder!\n\n{letter_final_version}"
            )

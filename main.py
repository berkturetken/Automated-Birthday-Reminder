# ---------- Automated Birthday Reminder (ABR) ----------
import datetime as dt
import pandas
import smtplib
from dotenv import load_dotenv
import os

# 1) Loading environment variables in local
local_key_path = "C:/Programming/Keys/key.txt"
load_dotenv(local_key_path)
# 2) Loading environment variables in PythonAnywhere
# local_key_path = os.path.expanduser('~')
# load_dotenv(os.path.join(local_key_path, '.env'))

# Constants
MY_EMAIL = os.getenv("berkturetken1_gmail")
PWD = os.getenv("berkturetken1_pwd")
receiver_emails = ["berk.turetken@aalto.fi", "buket.karakas@aalto.fi", "gokktugbasaran@gmail.com"]

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

        # Send the letter to the receivers
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PWD)

            for receiver in receiver_emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=receiver,
                    msg=f"Subject:Birthday Reminder!\n\n{letter_final_version}"
                )


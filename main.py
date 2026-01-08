import datetime as dt
import pandas
import smtplib
from dotenv import load_dotenv
import os
import argparse

load_dotenv()

# Constants
MY_EMAIL = os.getenv("berkturetken1_gmail")
PWD = os.getenv("berkturetken1_pwd")
receiver_emails = ["berkturetken1997@hotmail.com", "gokktugbasaran@gmail.com", "samiavger@gmail.com"]

# Parse command line arguments
parser = argparse.ArgumentParser(description='Automated Birthday Reminder - Check birthdays and send email notifications')
parser.add_argument('--date', type=str, help='Check birthdays for a specific date (format: DD.MM, e.g., 20.01)')
args = parser.parse_args()

# Read the csv file
csv_file_path = "docs/birthdays.csv"
if not os.path.exists(csv_file_path):
    print(f"Error: Birthday file '{csv_file_path}' not found!")
    print("Please create a 'birthdays.csv' file in the 'docs' folder with columns: name surname, month, day")
    exit(1)

data = pandas.read_csv(csv_file_path)
people_birthday_dates = data.to_dict(orient="records")

# Get the current month and day, or use provided date
if args.date:
    try:
        # Parse the date in DD.MM format (add a dummy year to avoid deprecation warning)
        check_date = dt.datetime.strptime(f"{args.date}.2026", "%d.%m.%Y")
        current_month = check_date.month
        current_day = check_date.day
        print(f"------------------------------------------------------------------------------\n{check_date} - Checking whether {current_day:02d}.{current_month:02d} is someone's birthday...")
    except ValueError:
        print(f"Error: Invalid date format '{args.date}'. Please use DD.MM format (e.g., 20.01)")
        exit(1)
else:
    now = dt.datetime.now()
    current_month = now.month
    current_day = now.day
    print(f"------------------------------------------------------------------------------\n{now} - Checking whether today is someone's birthday...")
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

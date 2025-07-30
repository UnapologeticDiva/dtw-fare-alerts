import requests
import smtplib
from email.mime.text import MIMEText
from datetime import date, timedelta

# ----------------------------
# CONFIGURATION
# ----------------------------
ORIGIN = "DTW"  # Detroit Metro
DESTINATIONS = ["JNB", "CPT", "NBO", "ACC", "CAI", "CMN"]  # Johannesburg, Cape Town, Nairobi, Accra, Cairo, Casablanca
THRESHOLD = 1200  # USD - alert if under this price

EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # You’ll create an App Password in Gmail settings
EMAIL_RECEIVER = "your_email@gmail.com"

# ----------------------------
# FLIGHT SEARCH FUNCTION (placeholder)
# ----------------------------
# NOTE: Real APIs like Skyscanner or Kiwi.com can be used.
# For demo purposes, this function simulates a fare result.

import random

def search_flights(origin, destination, start_date, end_date):
    # In real life: call Skyscanner API, Kiwi API, etc.
    # Here: simulate random prices for demo
    return random.randint(600, 2500)

# ----------------------------
# EMAIL ALERT FUNCTION
# ----------------------------

def send_alert(destination, price, start, end):
    subject = f"Mistake Fare Alert: {ORIGIN} to {destination} for ${price}"
    body = f"Found fare from {ORIGIN} to {destination} for ${price} between {start} and {end}. Book ASAP!"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

# ----------------------------
# MAIN LOOP
# ----------------------------

def main():
    today = date.today()
    for d in DESTINATIONS:
        start = today + timedelta(days=30)
        end = today + timedelta(days=45)
        price = search_flights(ORIGIN, d, start, end)
        print(f"Checked {ORIGIN}->{d}, Price: ${price}")
        if price < THRESHOLD:
            send_alert(d, price, start, end)

if __name__ == "__main__":
    main()

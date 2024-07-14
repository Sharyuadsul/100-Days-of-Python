import datetime as dt
import os
import smtplib
import random

my_mail="sharyuadsul19@gmail.com"
password = os.environ["APP_PASSWORD"]

now = dt.datetime.now()
if now.weekday()==0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
         connection.starttls()
         connection.login(user=my_mail, password=password)
         connection.sendmail(from_addr=my_mail,
                             to_addrs="gellerrmon002@gmail.com",
                             msg=f"Subject: Monday Motivation\n\n{quote}")

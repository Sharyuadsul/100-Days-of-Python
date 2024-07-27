import requests
from bs4 import BeautifulSoup
import smtplib

import os
from dotenv import load_dotenv
load_dotenv('../../.env')

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Full headers would look something like this
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

# Adding headers to the request
response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

whole_price = soup.find(class_="a-offscreen")
whole_price = whole_price.getText()
price_without_currency = whole_price.split("$")[1]
price_float = float(price_without_currency)

print(price_float)

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_float < BUY_PRICE:
    message = f"{title} is on sale for {whole_price}!"

MY_MAIL= os.getenv('MY_MAIL')
APP_PASSWORD = os.getenv('AMAZON_PRICE_TRACKER_APP_PASS')

conn = smtplib.SMTP("smtp.gmail.com", port=587)
conn.starttls()
conn.login(user=MY_MAIL, password=APP_PASSWORD)
conn.sendmail(
    from_addr=MY_MAIL,
    to_addrs=MY_MAIL,
    msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
)

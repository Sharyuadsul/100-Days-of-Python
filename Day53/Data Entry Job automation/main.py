from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


FORM_LINK = ("https://docs.google.com/forms/d/e/1FAIpQLSeiYM3"
             "-nFCbJrz07gfRax_FEDFWDoLaKe66B_RG-CU9iejSgA/viewform?usp=sf_link")
ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'

# Part 1 - Scrape the links, addresses, and prices of the rental properties

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(ZILLOW_URL,headers=header)
data = response.text
# print(data)

soup = BeautifulSoup(data, 'html.parser')
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links =[link["href"] for link in all_link_elements]
print(all_links)


all_prices_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace('/mo', '').split('+')[0] for price in all_prices_elements if '$' in price.text]
print(all_prices)

all_addresses_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace('|', '').strip() for address in all_addresses_elements]
print(all_addresses)

print(len(all_links))
print(len(all_addresses))
print(len(all_prices))



# Part 2 - Fill in the Google Form using Selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = chrome_options)

# for i in range(len(all_links)):
for i in range(len(all_links)):

    driver.get(FORM_LINK)
    time.sleep(2)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')


    address.send_keys(all_addresses[i])
    time.sleep(1)
    price.send_keys(all_prices[i])
    time.sleep(1)
    link.send_keys(all_links[i])
    time.sleep(1)
    submit.click()


driver.close()

"response_link = 'https://docs.google.com/spreadsheets/d/1bJGUMjB4zJI9ly0G-y4IVd0K_faQfKhb7-d2A67ReQA/edit?usp=sharing'"






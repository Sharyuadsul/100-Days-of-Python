from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
for i in range(5):
    cookie.click()

score = driver.find_element(By.CSS_SELECTOR, "#money")
print(score.text)

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

five_sec = time.time() + 5 # [seconds]
five_min = time.time()+ 5*60

while True:
    cookie.click()

    if time.time()>five_sec:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        stripped_prices = []

        for item in all_prices:
            element_price = item.text
            if element_price != "":
                cost = int(element_price.split("-")[1].strip().replace(",",""))
                stripped_prices.append(cost)

        cookie_upgrades = {}
        for i in range(len(stripped_prices)):
            cookie_upgrades[stripped_prices[i]] = item_ids[i]

        #get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element.replace(",", "")
        cookie_count = int(money_element)


        affordable_updrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count >cost:
                affordable_updrades[cost] = id


        max_upgrade = max(affordable_updrades)
        to_purchase_id = affordable_updrades[max_upgrade]
        print(f"max_upgrade: {max_upgrade} {to_purchase_id}")

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        five_sec = time.time() +5

        if time.time() > five_min:
            cookie_per_s = driver.find_element(by=By.ID, value="cps").text
            print(cookie_per_s)
            break

driver.quit()

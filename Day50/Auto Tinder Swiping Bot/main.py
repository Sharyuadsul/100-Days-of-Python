from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


load_dotenv('../../.env')

FACEBOOK_EMAIL = os.getenv('FACEBOOK_EMAIL')
FACEBOOK_PASSWORD= os.getenv('FACEBOOK_PASSWORD')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get('https://tinder.com/')

time.sleep(2)
log_in = driver.find_element(By.LINK_TEXT, 'Log in')
log_in.click()

time.sleep(2)
more_options = driver.find_element(By.CSS_SELECTOR, '.FlexColumn button')
more_options.click()

time.sleep(2)
facebook_login = driver.find_element(By.XPATH, '//*[@id="q-225181968"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)
# mail_field = driver.find_element(By.ID, 'email')
mail_field = driver.find_element(By.XPATH, '//*[@id="email"]')
mail_field.send_keys(FACEBOOK_EMAIL)
pass_field = driver.find_element(By.ID, 'pass')
pass_field.send_keys(FACEBOOK_PASSWORD, Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

i_accept = driver.find_element(By.XPATH, '//*[@id="q-225181968"]/div/div[2]/div/div/div[1]/div[1]/button')
i_accept.click()
time.sleep(2)

location_allow = driver.find_element(By.XPATH, '//*[@id="q-225181968"]/div/div[1]/div/div/div[3]/button[1]')
location_allow.click()
time.sleep(2)

notifications_button = driver.find_element(By.XPATH, value='//*[@id="q-225181968"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

time.sleep(10)

for n in range(100):
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='//*[@id="q1503199108"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div[3]/div/div[2]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()
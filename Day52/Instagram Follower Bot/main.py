from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException


from dotenv import load_dotenv
load_dotenv('../../.env')

INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD= os.getenv('INSTAGRAM_PASSWORD')
TARGET_ACCOUNT = 'chefsteps'

class InstagramFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(INSTAGRAM_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(1)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)


        time.sleep(6)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(),'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(),'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()



    def find_followers(self):
        time.sleep(5)
        self.driver.get('https://www.instagram.com/chefsteps/followers')

        time.sleep(5)
        modal_path = "/html/body/div[6]/div/div/div[2]/div/div/div/div[2]"
    
        modal = self.driver.find_element(By.XPATH, modal_path)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)



    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

bot = InstagramFollower()
bot.login()
bot.find_followers()
bot.follow()

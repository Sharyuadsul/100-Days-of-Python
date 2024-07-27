from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
from selenium.common.exceptions import NoSuchElementException

load_dotenv('../../.env')

ACCOUNT_EMAIL = os.getenv('LINKEDIN_EMAIL')
ACCOUNT_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
PHONE = os.getenv('PHONE')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location="
           "Pune%25%22%222C%20Maharashtra%2C%20India&geoId=114806696&trk=public_jobs_jobs-"
           "search-bar_%22%22search-submit&position=1&pageNum=0&original_referer=")



# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
# input("Press Enter when you have solved the Captcha")

save_button = driver.find_elements(By.CLASS_NAME, "mt5 button")
save = save_button[1].click()


# def abort_application():
#     # Click Close Button
#     close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#     close_button.click()
#
#     time.sleep(2)
#     # Click Discard Button
#     discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
#     discard_button.click()


# time.sleep(5)
# all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
#
# # Apply for Jobs
# for listing in all_listings:
#     print("Opening Listing")
#     listing.click()
#     time.sleep(2)
#     try:
#         # Click Apply Button
#         apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
#         apply_button.click()
#
#         # Insert Phone Number
#         # Find an <input> element where the id contains phoneNumber
#         time.sleep(5)
#         phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         # Check the Submit Button
#         submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             abort_application()
#             print("Complex application, skipped.")
#             continue
#         else:
#             # Click Submit Button
#             print("Submitting job application")
#             submit_button.click()
#
#         time.sleep(2)
#         # Click Close Button
#         close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#         close_button.click()
#
#     except NoSuchElementException:
#         abort_application()
#         print("No application button, skipped.")
#         continue
#
# time.sleep(5)
# driver.quit()

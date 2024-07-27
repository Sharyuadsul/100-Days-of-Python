from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Sharyu")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Adsul")

email = driver.find_element(By.NAME, "email")
email.send_keys("sharyuadsul19@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()


# driver.quit()
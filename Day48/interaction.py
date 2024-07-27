from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#CLICKING
# score = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # print(score.text)
# score.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

#TYPING
search_icon = driver.find_element(By.CSS_SELECTOR, "#p-search a")
search_icon.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()
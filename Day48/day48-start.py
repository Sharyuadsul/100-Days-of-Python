# import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#
# price_doller = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
#
# print(f"The price is {price_doller}.{price_cents}")

driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, "submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
#
# submit_website_bug_link = driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_website_bug_link.text)

all_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
all_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events={}
for n in range(len(all_events)):
    events[n]={
        "time":all_dates[n].text,
        "name":all_events[n].text,
    }

print(events)


# driver.close()
driver.quit()




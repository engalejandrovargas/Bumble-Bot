from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# DATA FROM YOUR ACCOUNT

ACCOUNT_EMAIL = "your@email.com"
ACCOUNT_PASSWORD = "Password"
PHONE = "+600000000"

# SELENIUM CONFIGURATION

chrome_driver_path = 'C:\Selenium\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://bumble.com/app")

time.sleep(5)

# LOGIN USING FACEBOOK

login_face = driver.find_element_by_xpath(
    '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')
login_face.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# FACEBOOK FORM

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
time.sleep(1)
email.send_keys(ACCOUNT_EMAIL)
time.sleep(1)
password.send_keys(ACCOUNT_PASSWORD)
time.sleep(1)
password.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)

time.sleep(10)

# CLICK LIKE BUTTON - Match the firts 10 profiles, change as you wish =)

for x in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]')
        like_button.click()
    except NoSuchElementException:
        continue

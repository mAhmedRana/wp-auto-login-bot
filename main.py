from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# fill in random username and password (for 1st Time)
usernameStr = 'aleksandra'
passwordStr = 'wjfTFZzzVFgz6AUj'

# fill in random username and password (for 2nd time and afterwords)
usernameLoopStr = 'adelaida'
passwordLoopStr = 'nxJ2MA7e6_NBT'

# starting browser
browser = webdriver.Chrome()

# fill in the website url
browser.get(('https://YourWordPressWebsiteAdminURL'))

# fill in username and hit the next button
username = browser.find_element_by_id('user_login')
time.sleep(10)
username.send_keys(usernameStr)

# fill in password and hit the next button

password = browser.find_element_by_id('user_pass')
time.sleep(10)
password.send_keys(passwordStr)
 
# submit information 
signInButton = browser.find_element_by_class_name('wp-submit')
time.sleep(2)
signInButton.click()

# infinite loop if you want to spam.
def repeat():
    while 1 == 1:

        browser.find_element_by_id('input_1').clear()

        username = browser.find_element_by_id('user_login')
        time.sleep(10)
        username.send_keys(usernameLoopStr)

        password = browser.find_element_by_id('user_pass')
        time.sleep(10)
        password.send_keys(passwordLoopStr)
 
        signInButton = browser.find_element_by_class_name('wp-submit')
        time.sleep(5)
        signInButton.click()

repeat()

from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
username = "preethibollineni55@gmail.com"
with open ('password.txt','r') as file:
    password = file.read()

# initialize the Chrome driver
driver = webdriver.Chrome()
# head to amazon login page
driver.get("https://www.amazon.com")

signin = driver.find_element_by_id("nav-link-accountList-nav-line-1").click()

# find username/email field and send the username itself to the input field
username_textbox =  driver.find_element_by_id("ap_email")
username_textbox.send_keys(username)

continue_ = driver.find_element_by_id("continue").click()

# find password input field and insert password as well
password_textbox =  driver.find_element_by_id("ap_password")
password_textbox.send_keys(password)

# click login button
button = driver.find_element_by_id("signInSubmit")
button.submit()

error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements_by_class_name("flash-error")
# print the errors optionally
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("Login failed")
else:
    print("Login successful")

# close the driver
#driver.close()

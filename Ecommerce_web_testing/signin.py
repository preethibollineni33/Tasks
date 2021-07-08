from selenium import webdriver

username = "preethibollineni55@gmail.com"

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

with open ('password.txt','r') as file:
    password = file.read()

signin = driver.find_element_by_id("nav-link-accountList-nav-line-1").click()

username_textbox =  driver.find_element_by_id("ap_email")
username_textbox.send_keys(username)

continue_ = driver.find_element_by_id("continue").click()

password_textbox =  driver.find_element_by_id("ap_password")
password_textbox.send_keys(password)

button = driver.find_element_by_id("signInSubmit")
button.submit()
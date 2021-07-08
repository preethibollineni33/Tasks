#Purpose of the project
###############################################################################################################
#This script has been designed to test Ecommerce website automation testing 
#using python-selenium
###############################################################################################################

##################################################################################################
#Below points has been considered in the Script.
##################################################################################################
#1.Write the python code with selenium webdriver using chrome
##################################################################################################

#####################################  Script Details  ############################################
#Script Name             :         ecommerce.py
#Script Version          :         1.0
#Prepared By             :         preethi.bollineni@infinite.com
#Create Date             :         15-06-2021
#Last Modification Date  :         18-06-2021
####################################################################################################
#Importing modules
#import webdriver modules navigate to chrome 
from selenium.webdriver import Chrome,ChromeOptions
import time
from selenium.webdriver.common.action_chains import ActionChains 
#importing module
import logging
  
#Create and configure logger
logging.basicConfig(filename="class.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)
  
#Creating an object
logger=logging.getLogger()
  
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)
###########################################################################################

logging.info('Execution of script has started')
DATA = {"Driver": Chrome("/usr/bin/chromedriver"),
        "URL": "https://www.amazon.com",
        "username": "preethibollineni55@gmail.com",
        "password": "Preethi@12344",
        "name":"preethi"}
EXPECTED_COLOR = "rgba(221, 0, 0, 1)"

logging.info('amazon class has been created')
class AmazonTest:

    def __init__(self):

        self.driver = DATA["Driver"]
        self.URL = DATA["URL"]
        self.user = DATA["username"]
        self.password = DATA["password"]
        self.name = DATA['name']
        self.Is_loggedin = False

    def getPage(self):
        '''Method to get the current page'''
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.current_url = self.driver.current_url
        print(self.current_url)
        logging.info("To print the current url")
        return self.current_url
        logging.info('gets to amazon signin page using get() method and returns current_url()')

    def email_password_signIn(self):
        '''Method fetches the email and password and signed to amazon account'''
        logging.info('signIn amazon account has started')
        self.nav_account_list = self.driver.find_element_by_id(
            "nav-link-accountList").click()

        self.user_input = self.driver.find_element_by_id("ap_email")
        self.user_input.send_keys(self.user)
        self.continue_button = self.driver.find_element_by_id("continue")
        self.continue_button.click()
        logging.info('email has been fetched')

        self.pass_input = self.driver.find_element_by_id("ap_password")
        self.pass_input.send_keys(self.password)
        self.submit_button = self.driver.find_element_by_id("signInSubmit")
        self.submit_button.click()
        logging.info('password has been fetched')

        self.Is_loggedin = True
        return 'successfully logged in'
        logging.info('successfully logged into account')

    def validation(self):
        '''Method to check for validation'''
        action = ActionChains(self.driver)
        time.sleep(2)

        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
        action.move_to_element(firstmenu).perform()
        time.sleep(2)

        secondmenu = self.driver.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a')
        secondmenu.click()
        time.sleep(2)

        signupbutton = self.driver.find_element_by_id("continue").click()
        time.sleep(2)

        username = self.driver.find_element_by_id('ap_email')
        if "error" in username.get_attribute('outerHTML'):
            obtained_color = username.value_of_css_property('border-bottom-color')
            if not self.check_color(obtained_color, "rgba(222, 20,33, 1)"):
                print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")

        password = self.driver.find_element_by_id('ap_password')
        if "error" in password.get_attribute('outerHTML'):
            obtained_color = password.value_of_css_property('border-bottom-color')
            if not self.check_color(obtained_color, "rgba(222, 20, 33, 1)"):
                print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")

        error_messages = ["At least 3 characters",
                            "Invalid Email", "At least 6 characters"]
        message_body_html_elements = self.driver.find_elements_by_class_name('msg-body')
        for msg in message_body_html_elements:
            error_msg = msg.get_attribute('innerHTML').split("span")[1][1:-2]
            if error_msg not in error_messages:
                print(f"{msg.get_attribute('outerHTML')} is missing error message")

        self.close_driver()   
        return obtained_color
        
       
    #it checks whether the color and original color are same or not
    def check_color(self, color, orginal_color):
        return color == orginal_color

    #this methods will change amazon account password 
    def forgot_password(self):
        logging.info('changing the password')
        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
        firstmenu.click()
        time.sleep(3)
        
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys("preethibollineni55@gmail.com")
        time.sleep(3)

        continue_button = self.driver.find_element_by_id("continue").click()
        time.sleep(2)

        forgot_pass = self.driver.find_element_by_xpath('//*[@id="auth-fpp-link-bottom"]').click()
        time.sleep(2)
        
        continue_button = self.driver.find_element_by_id("continue").click()
        time.sleep(2)

        otp = self.driver.find_element_by_xpath('//*[@id="cvf-input-code"]')
        time.sleep(20)
        #Creating new password
        new_passwd = "********"
        retype_passwd = "********"

        new_password = self.driver.find_element_by_name("password").send_keys(new_passwd)
        retype_password = self.driver.find_element_by_name("passwordCheck").send_keys(retype_passwd)
        time.sleep(2)
        
        signin = self.driver.find_element_by_id("continue").click()
        time.sleep(5)
        if new_passwd == retype_passwd:
            return retype_passwd
            logging.info('password has been changed')
        else:
            print('password is not matching')
            return "password is not matching"
            logging.info('password is not matching')

    #this method trigged to signed into amazons account
    def keep_me_signedin(self):
        logging.info('gets to sign in page')
        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
        firstmenu.click()
        time.sleep(3)
        logging.info('email has been fetched')
        # find username/email field and send the username itself to the input field
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys("preethibollineni55@gmail.com")
        time.sleep(3)

        continue_button = self.driver.find_element_by_id("continue").click()
        time.sleep(2)
        
        # find password input field and insert password as well
        keep_me_signed = self.driver.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div[1]/div/div/form/div/div[2]/div/div/label/div/label/input')
        keep_me_signed.click()
        logging.info('password has been fetched')
        password = self.driver.find_element_by_name("password")
        password.send_keys(self.open_txt_file())
        time.sleep(2)
        # click login button
        signin = self.driver.find_element_by_id("signInSubmit").click()
        time.sleep(3)

        self.close_driver()
        return 'signed successfully'
        logging.info('logged in successfully')

    #this method fetches the password from txt file    
    def open_txt_file(self):
        with open("password.txt", "r") as fr:
            Password = fr.read()
        return Password
        logging.info('password fetched from txt file')

    #this method will close the driver
    def close_driver(self):
        self.driver.close()
        logging.info('amazon page is closed')
    
a = AmazonTest()
#a.getPage()
#a.email_password_signIn()
#a.validation()
#a.validate_password()
#a.forgot_password()
a.keep_me_signedin()


        
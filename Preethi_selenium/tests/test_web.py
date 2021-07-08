#Purpose of the project
##############################################################################################################################
#This script has been designed to do python test automation  using pytest,selenium
##############################################################################################################################

##############################################################################################################################
#Below points has been considered in the Script.
##############################################################################################################################
#1.Install selenium  web driver using Python and Chrome
#2.Write Python Code which goes to a particular URL,and when enter the search phrase, the Results appear on the results page.
#The search phrase appears in search bar.
#3.Refactor the code using the Page Object Pattern I.e put comments ,use of class, Structured Programming 
#4.Write code to read config files in Python Selenium Tests and add new browsers and make sure the code works in new browsers
#5.Generate html report and pdf file.
#6.Run the project with 4 test threads.
##############################################################################################################################

#####################################  Script Details  #######################################################################
#Script Name             :         test_web.py
#Script Version          :         1.0
#Prepared By             :         preethi.bollineni@infinite.com
#Create Date             :         03-06-2021
#Last Modification Date  :         07-06-2021
###############################################################################################################################

#Importing modules
import pytest
import json
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from selenium.webdriver import Chrome, Firefox
import logging
logging.basicConfig(filename='preethi1.log',format='%(asctime)s %(message)s',filemode='w',level=logging.INFO)
#Creating an object
logger=logging.getLogger()
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

################################################################################################################################
CONFIG_PATH = 'config.json'
logging.info("setting the path")
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

@pytest.fixture(scope='session')
def config():
  #Read the JSON config file and returns it as a parsed dict
  with open(CONFIG_PATH) as config_file:
    data = json.load(config_file)
  return data

@pytest.fixture(scope='session')
def config_browser(config):
  #Validate and return the browser choice from the config data
  if 'browser' not in config:
    raise Exception('The config file does not contain "browser"')
  elif config['browser'] not in SUPPORTED_BROWSERS:
    raise Exception(f'"{config["browser"]}" is not a supported browser')
  return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
  #Validate and return the wait time from the config data
  return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

@pytest.fixture
def browser(config_browser, config_wait_time):
  # Initialize WebDriver
  if config_browser == 'chrome':
    driver = Chrome()
  elif config_browser == 'firefox':
    driver = Firefox()
  else:
    raise Exception(f'"{config_browser}" is not a supported browser')

  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(config_wait_time)
  
  # Return the driver object at the end of setup
  yield driver
  
  # For cleanup, quit the driver
  driver.quit()

def test_basic_duckduckgo_search(browser):
  # Set up test case data
  PHRASE = 'panda'
  # Search for the phrase
  search_page = DuckDuckGoSearchPage(browser)
  logging.info("searching for browser")
  
  search_page.load()
  logging.info("Loading the browser")

  search_page.search(PHRASE)
  logging.info("searching the phrase in the browser")

  # Verify that results appear
  result_page = DuckDuckGoResultPage(browser)
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE

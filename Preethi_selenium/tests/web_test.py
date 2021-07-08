from src.testproject.sdk.drivers import webdriver
import logging
logging.basicConfig(filename='preethi1.log',format='%(asctime)s %(message)s',filemode='w',level=logging.INFO)
#Creating an object
logger=logging.getLogger()
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

################################################################################################################################
def simple_test():
    logging.info("providing the developer token")
    driver = webdriver.Chrome(token='R_dDnFdBzHujjj-FpMIExQxdj08i0y6cl4mKHeIdR2k1')
    logger.info("providing the url of testproject")
    driver.get("https://example.testproject.io/web/")
    logging.info("providing username and password")
    driver.find_element_by_css_selector("#name").send_keys("Preethi")
    driver.find_element_by_css_selector("#password").send_keys("12345")
    driver.find_element_by_css_selector("#login").click()
    passed = driver.find_element_by_css_selector("#logout").is_displayed()
    print("Test passed") if passed else print("Test failed")
    driver.quit()
if __name__ == "__main__":
    simple_test()

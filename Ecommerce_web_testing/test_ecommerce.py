#Purpose of the project
#####################################################################################################
#This script has been designed to test the Ecommerce website using Automation Testing
#####################################################################################################

#####################################################################################################
#Below points has been considered in the Script.
#####################################################################################################
#1.Write Testcases for both success and failure conditions.
######################################################################################################

#####################################  Script Details  ###############################################
#Script Name             :         test_classroom.py
#Script Version          :         1.0
#Prepared By             :         preethi.bollineni@infinite.com
#Create Date             :         15-06-2021
#Last Modification Date  :         18-06-2021
#######################################################################################################
#Importing modules
import pytest
import logging
# Creating an logging object
logger=logging.getLogger(__name__)
#from colour import Color
import ecommerce

# Creating an instance for the AmazonTest class
ecommerce = AmazonTest()

# writing test cases to check the functionalities of ecommerce website.
class TestEcommerce:

    def test_getPage(self): 
        '''Test method for getPage to check the correct page'''
        # Assert condition to get the result from current page
        assert ecommerce.getPage() == "https://www.amazon.in/"
        logger.info('Testing for getpage is done successfully')

    def test_email_password_signIn(self):
        '''Test method for to check valid email and password'''
        #Assert condition to check for signin
        assert ecommerce.email_password_signIn() =='successfully logged in'
        logging.info("signin to amazon account is done successfully")

    def test_validation(self):
        '''Test method to check for username and password'''
        #Assert condition to check for validation.
        assert ecommerce.validation() == 'rgba(221, 0, 0, 1)'
        logger.info('Teting for validation is done')

    def test_forgetpassword(self):
        '''Test method to check for forget password functionality'''
        #Assert condition to check the result.
        assert ecommerce.forget_password() == 1
        logger.info('Testing for forgot password is done successfully')

    def test_keep_me_signedin(self):
        '''Test method for keep_me_signed_in functionality'''
        # Assert condition to check the result
        assert ecommerce.keep_me_signedin() == 'signed successfully'
        logger.info('Testing for signed_in is done successfully')

if __name__=='__main__':
    pytest.main(args=['-s', os.path.abspath(__file__)])
   
    

#Purpose of the project
##############################################################################################################################
#This script has been designed to write python test scripts for create,list,get,update,patch 
#and delete methods using pytest.
##############################################################################################################################

##############################################################################################################################
#Below points has been considered in the Script.
##############################################################################################################################
#1.Write Test Scripts for both positive and negative cases
#2.Use Loggers to print all the information on screen while executing and in log files
##############################################################################################################################

#####################################  Script Details  ########################################################################
#Script Name             :         test_classroom.py
#Script Version          :         1.0
#Prepared By             :         preethi.bollineni@infinite.com
#Create Date             :         09-06-2021
#Last Modification Date  :         14-06-2021
###############################################################################################################################
#Importing modules
import quickstart
import methods
import pytest
import exceptions
from exceptions import (list_courses,get_course)
import logging
logger=logging.getLogger(__name__)

course_id=methods.list_courses()
logging.info("stores the list of courses")
print(course_id)
def test_courses_list():
    '''This test method checks positive test case for list method'''
    #providing particular id to check in list
    id='360055335405'
    assert id in course_id,"Provided id is not in list"
    logging.info("condition to check that particular id is present in list of courses or not")

def test_list_negative_course():
    #id='360675352659'
    #assert id not in course_id
    with pytest.raises(Exception) as exp_info:
        #exceptions.id_checking(id)
        #len(methods.list_courses(course_id[0])) != 0
        #list_courses(course_id[0]!=0)
        logging.info(str(exp_info.value))
    print(str(exp_info.value))   

def test_create_course():
    '''This method checks positive testcase for create method'''
    #Get the particular course id 
    res = methods.get_course('360675352658')
    assert (dict,type(res)),"Type of course is not dict type"
    logging.info("checks the type of course")

def test_create_course1():
    '''This method checks negative testcase for create method'''
    #Get the particular course id 
    res = methods.get_course('360675352658')
    assert (dict!=type(res)),"Type of course is dict type"
    logging.info("checks the type of course")

def test_get_course():
    '''This test method checks positive testcase for get method'''
    #assert methods.get_course(360055335405)!=0
    assert methods.get_course('360675352658')!='7th grade maths','course not found'
    logging.info("get the particular id and checks it is equal to zero or not")

def test_get_negative_course():
    with pytest.raises(Exception) as exp_info:
        #len(methods.list_courses(course_id[0])) != 0
        #get_course(course_id[0]!='5th grade maths')
        logging.info(str(exp_info.value))
    print(str(exp_info.value)) 

def test_update_course():
    '''This test method checks positve testcase for update method'''
    update_1=methods.update_course('360675352658')
    list_1=methods.get_course('360675352658')
    assert update_1==list_1[1],'updated course are not same'
    logging.info("checks the updated course room no")

def test_patch_course():
    '''This test method checks positive test case for patch method'''
    #Updating the section and room for two ids
    update_id1=methods.update_course('360055335405')
    update_id2=methods.update_course('355971717862')
    assert update_id1==update_id2,'course ids are not same'
    logging.info("checks the two updated ids are same or not")

if __name__=='__main__':
    pytest.main(args=['-s', os.path.abspath(__file__)])
   
    


        
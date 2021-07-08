import logging
import methods
import pytest

#logger=logging.getLogger(__name__)

logging.info("Execution of code starts from here.")

logging.info("Assigned all the course ids to a variable")
course_id = methods.list_courses()
#####################################################################################################

'''This test case is used whether the id is created or not'''
def test_create_course():
    logging.info("Method for creating a course.")
    res = methods.get_course(course_id[0])
    assert dict,type(res)
    logging.info("Test case for create course is successfully passed.")

'''This negative test case is used whether the id is created or not'''

def test_negative_create():
    logging.info("Method for creating a course.")
    res = methods.get_course(course_id[0])
    assert dict!=type(res)
    logging.info("Negative Test case for create course is successfully passed.")

#########################################################################################################
'''Test case for list out the course id's'''

def test_list_course():
    logging.info("Checking whether the id is present in the list or not")
    id = course_id[1]
    res = methods.list_courses()
    assert id in course_id, "course_id is not provided in the list"
    assert list == type(res), 'return type of the function is not list'
    logging.info("Test case for for list out the id's is passed successfully")

'''Negative Test case for list out the course id's'''

def test_negative_list():
    logging.info("Checking whether the id is present in the list or not")
    id = '360052810656' 
    assert id not in  course_id, "course_id is provided in the list"
    logging.info("Negative Test case for list method for list out the id's is passed successfully")

#######################################################################################################

'''Test case for get the particular course id'''

def test_get_course():
    logging.info("Check the condition whether the id is not equals to 16")
    res = methods.get_course(course_id[0])
    #assert len(res)>0, 'length is less than zero no course is created'
    assert methods.get_course(course_id[0])[0] == '10th Grades Social', 'course not found'
    assert type(res[0])==dict, 'return type of the function is not dict'
    logging.info("Test case for get method is passed successfully") 

'''Negative Test case for get the particular course id'''

def test_negative_get():
    logging.info("Check the condition whether the id is not equals to 16")
    assert methods.get_course(course_id[0])[1] != '10th Grades Socials' 
    logging.info("Negative Test case for get method is passed successfully")
#######################################################################################################

'''Test case for update the data for a particular id'''

def test_update_course():
    '''logging.info("Performing the test case for updating the data for specific id.")
    update_id1= method.update_courses(course_id[1])
    list_room = method.get_course(course_id[1])
    print(update_id1)
    print(list_room)
    assert(update_id1 == list_room[2])
    logging.info("Test case for update method is passed successfully")'''
    data1 = method.get_course(course_id[2])
    data2 = method.update_courses(course_id[2])
    logger.info(data2)
    logger.info(data1)
    assert str(data1[0][0])==data2[0], "name are equal and course hasn't been updated"
    assert str(data1[0][1])==data2[1], "room numbers are equal and course hasn't been updated"

'''Negative Test case for update the data for a particular id'''
def test_negative_update():
    logging.info("Performing the negative test case for updating the data for specific id.")
    update_id1 = methods.update_course(course_id[0])
    list_room = methods.get_course(course_id[0])
    print(update_id1)
    print(list_room)
    assert (update_id1 != list_room[2])
    logging.info("Negative Test case for update method is passed successfully")

########################################################################################################

''' Tesat case for delete the particular id present in list'''
def test_delete_course():
    logger.info('Execution entered into test_delete_check function')
    method.delete_course(course_id)
    id = '360769114563'
    assert id not in course_id, 'Id has not deleted successfully'
    logger.info('Execution successfully completed for function test_delete_check')

def test_negative_delete():
    logging.info('Execution entered into test_delete_check function')
    method.delete_course(course_id)
    id = '360769115825'
    assert id in course_id, 'Id has not deleted successfully'
    logger.info('Execution successfully completed for function test_delete_check')

###########################################################################################################  
'''Test case for patch update the particular ids'''

def test_patch_course():
    '''logging.info("Performing the test case for patch method based on ids and update.")
    patch_id1 = method.patch_update(course_id[2])
    patch_id2 = method.patch_update(course_id[3])
    print(patch_id1)
    print(patch_id2)
    assert patch_id1 == patch_id2
    logging.info("test case for updation of the course id's is successfully passed.")'''
    method.patch_update(course_id[3])
    data1 = method.get_course(course_id[3])
    data2 = method.patch_update(course_id[3])
    assert 'section' in data1[0].keys(), "section are equal and course hasn't been updated"
    assert str(data1[0]['room'])==data2[1], "room numbers are equal and course hasn't been updated"
    logger.info('Execution successfully completed for function test_patch_update')

''' Negative Test case for patch update the particular ids'''

def test_negative_patch():
    logging.info("Performing the negative test case for patch method based on ids and update.")
    patch_id1 = method.patch_update(course_id[0])
    patch_id2 = method.patch_update(course_id[1])
    print(patch_id1)
    print(patch_id2)
    assert patch_id1 != patch_id2
    logging.info("Negative test case for updation of the course id's is successfully passed.")
###################################################################################################

logging.info("Execution of code stops here.")

#if __name__ == '__main__':
#pytest.main(args=['-sv', os.path.abspath(__file__)])
    
from apiclient import errors

from methods import main
from methods import (list_courses,get_course,update_course,patch_course)
class NotDeleted(Exception):
    pass
class NegativeIndexError(Exception):
    pass
class Successful(Exception):
    pass
class ValueNotEqual(Exception):
    pass
service=main()
def list_courses():
    #if len(list_courses())==0:
        if len(course_id)>12 or len(course_id)<12:
            raise ValueNotEqual("Length of id must be 12")

def get_course(course_id):
    if type(get_course(id))!=tuple or type(get_course(id)[0])!=dict:
        raise TypeError("Must return a given datatype")
    elif str(id)!=get_course(id)[0]['id']:
        raise ValueNotEqual("The id is not found or not created")
    elif get_course(id)==None:
        raise TypeError("No course found with given id")
    else:
        msg="Successfully Created"
        return msg
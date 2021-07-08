#Purpose of the project
##############################################################################################################################
#This script has been designed to write python test methods for create,list,get,update,patch 
#and delete methods using pytest.
##############################################################################################################################

##############################################################################################################################
#Below points has been considered in the Script.
##############################################################################################################################
#1.Use Loggers to print all the information on screen while executing and in log files
##############################################################################################################################

#####################################  Script Details  #######################################################################
#Script Name             :         methods.py
#Script Version          :         1.0
#Prepared By             :         preethi.bollineni@infinite.com
#Create Date             :         09-06-2021
#Last Modification Date  :         13-06-2021
###############################################################################################################################
#Importing modules
import quickstart
from quickstart import main
import logging
from googleapiclient import errors
logging.basicConfig(filename='class.log',format='%(asctime)s %(message)s',filemode='w',level=logging.INFO)
#Creating an object
logger=logging.getLogger()
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

################################################################################################################################
service=main()
def create_course():
    """ Creates a single Classroom course. """
    service = main()
    #START classroom_create_course
    course = {
        'name': '8th Grade Maths',
        'section': 'Period 3',
        'descriptionHeading': 'Welcome to 9th Grade Maths',
        'description': """We'll be learning about about the
                         structure of living creatures from a
                         combination of textbooks, guest lectures,
                         and lab work. Expect to be excited!""",
        'room': '301',
        'ownerId': 'me',
        'courseState': 'PROVISIONED'
        }
    #logging.info("creating a course")
    try:
        course = service.courses().create(body=course).execute()
        print('Course created: %s %s' % (course.get('name'), course.get('id')))
    except:
        return None

def get_course(course_id):
    '''Get the particular course'''
    service=main()
    try:
        course=service.courses().get(id=course_id).execute()
        #return(course,course['name'])
        print('Course "{%s}" found.' % course.get('name'))
        logging.info("getting the course name if course was found")
    except errors.HttpError as error:
        print('Course with id "{%s}" not found'% course_id)
        #return None

def list_courses():
        """ Lists all classroom courses. """
        service = main()
        # [START classroom_list_courses]
        try:
            courses = []
            page_token = None
            #Creating empty list to store the list of course ids
            lst=[]
            while True:
                response = service.courses().list(pageToken=page_token,
                                                pageSize=100).execute()
                courses.extend(response.get('courses', []))
                page_token = response.get('nextPageToken', None)
                if not page_token:
                    break
            if not courses:
                print('No courses found.')
                #return None
            else:
                print('Courses:')
                for course in courses:
                    ids=course['id']
                    lst.append(ids)
                    print(course.get('name'), course.get('id'),course.get('section'))
                return lst
        # [END classroom_list_courses]
        except:
            raise Exception('list length is not equal to zero')

def update_course(course_id):
    """ Updates the section and room of Google Classroom. """
    #lst=list_courses()
    service = main()
    # [START classroom_update_course]
    course = service.courses().get(id=course_id).execute()
    #course={}
    course['section'] = 'Period 20'
    course['room'] = '22'
    course = service.courses().update(id=course_id, body=course).execute()
    print('Course %s updated.' % course.get('name'))
    #return (course['section'],course['room'])
    #logging.info("Updated section and room no successfully")
    # [END classroom_update_course]

def patch_course(course_id):
        """ Creates a course with alias specification. """
        service = main()
        # [START classroom_patch_course]
        course = {
            'section': 'Period 3',
            'room': '302'
        }
        course = service.courses().patch(id=course_id,
                                            updateMask='section,room',
                                            body=course).execute()
        print('Course "%s" updated.' % course.get('name'))
        return (course['section'],course['room'])
        # [END classroom_patch_course]

def delete_course(course_id):
    courses_to_delete = list_courses()
    if course_id in courses_to_delete:
        try:
            course = service.courses().get(id=course_id).execute()
            course['courseState'] = 'ARCHIVED'
            course = service.courses().delete(id=course_id).execute()
            print('course deleted')
        except errors.HttpError as error:
            print('Unable to delete file %s' % course_id)
    else:
        print('delete')

if __name__ == '__main__':
    #main()
    #create_course()
    #get_course(360675352658)
    #list_courses()
    #update_course(360055335405)
    #patch_course(360047907525)
    delete_course('360047907525')
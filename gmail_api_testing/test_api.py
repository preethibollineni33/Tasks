from __future__ import print_function
import os.path
from webbrowser import get
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pytest

# If modifying these scopes, delete the file token.json.
SCOPES =  ['https://mail.google.com/']

def get_main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail messages.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    #Returning the service object
    return service

#To get the ids and threadids from the accessed mail
def list_mail():
    service = get_main()
    results = service.users().messages().list(userId='me', includeSpamTrash=None).execute()
    return results.get('messages', [])

#To get the contents of the id
def get_email_content(message_id):
    service = get_main()
    data = service.users().messages().get(userId='me', id=message_id ).execute()
    return data

#To modify the email contents 
def modify_email(message_id):
    body1 = {
            "addLabelIds": [ 
                "STARRED"
            ],
            "removeLabelIds": [ 
                "CATEGORY_UPDATES"
            ],
        }
    service = get_main()
    data = service.users().messages().modify(userId='me', id=message_id, body=body1).execute()
    return data

list_of_ids_tobe_modified = ['179a452609187490',
                            '179a4201e5d2296f',
                            '179a3bb1b674ef82',
                            '179a3b86a9141323',
                            '179a3af638ee4c51']
#To batch modify the email contents 
def batch_modify_email():    
    
    body1 = {
            "ids":list_of_ids_tobe_modified,
            "addLabelIds": [ 
            "STARRED"
            ],
            "removeLabelIds": [ 
                "CATEGORY_UPDATES",
                "SPAM"
            ],
        }
    service = get_main()
    data = service.users().messages().batchModify(userId='me', body=body1).execute()
    return data

#To delete an id from the list
def delete_email(message_id):
    service = get_main()
    data = service.users().messages().delete(userId='me', id=message_id).execute()
    return data

#To test whether the test_list_check method gives the expected output or not.
def test_list_check():

    #Collecting all the emails from the function list_mail( ) and assigning it to a value
    final_data = list_mail()

    #Checking for the condition
    assert len(final_data) >=0


#To test whether the test_trash_check method to check whether the id is in trash or not
def test_trash_check():
    input_id = '17993fdc7f37cd8c'
    #Collecting  the email content from the function get_email_content() and assigning it to a value.
    final_data = get_email_content(input_id)
    #checking for the condition
    assert 'TRASH' in final_data['labelIds'], 'mail not found in trash'

#To test whether the test_untrash_check method to check whether the id is in inbox or not
def test_untrash_check():
    input_id = '17993fdc7f37cd8c'
    #Collecting  the email content from the function get_email_content() and assigning it to a value.
    final_data = get_email_content(input_id)
    #Checking for the condition
    assert 'INBOX' in final_data['labelIds'], 'mail is not in trash'
    
#To test whether the test_modify_check method to check whether the content in id modified or not
def test_modify_email():
    input_id = '179a6d9ee692e69f'
    #Getting the original contents
    original_data = get_email_content(input_id)
    #Modifying the contents in given id's
    modify_email(input_id)
    #Getting the modified contents
    modified_data = get_email_content(input_id)
    #Checking the condition
    assert modified_data != original_data, 'data modified'

#To test whether the test_get_email method to check whether  content is present or not
def test_get_email():
    input_id = '179a6d9ee692e69f'
    #collecting the contents of the given id
    data = get_email_content(input_id)
    #Checking for the given condition
    assert len(data) != 0, 'no content there or id not found'

#To test whether the test_delete_check method to check whether  id is deleted or not
def test_delete_check():
    input_id = '179a6d9ee692e69f'
    data = list_mail()
    #Collecting the list of id's
    lst = [ message['id'] for message in data]
    #Condition for checking whether id is deleted or not
    assert input_id in lst, 'Not Deleted'

#To test whether the test_batch_modify_check method to check whether  id is modified or not
def test_batch_modify_check():
    #Creating an empty dictionary to store the values
    dictt_of_original_content = {}
    #Travesing through the list and assing as key value pair to dict
    for i in list_of_ids_tobe_modified:
        dictt_of_original_content.setdefault(i, get_email_content(i))

    #Modifying the content of data in given id
    batch_modify_email()
    for i in list_of_ids_tobe_modified:
        #Checking for the condition
        assert get_email_content(i) != dictt_of_original_content[i], f'Mail not changed for id{i}'








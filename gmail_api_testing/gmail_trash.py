from __future__ import print_function
import os.path
import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']

def get_gmail_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
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
    return service

#List the messages in the user's mail box
def get_email_list():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', maxResults=15).execute()
    return results.get('messages', [])

#Gets the specified message
def get_email_content(message_id):
    service = get_gmail_service()
    user_data = service.users().messages().get(userId='me', id=message_id).execute()
    return user_data

#Moves the specified message to trash
def get_email_trash(message_id):
    service = get_gmail_service()
    user_data1 = service.users().messages().trash(userId='me', id=message_id).execute()
    return user_data1

#Removes the specified message from the trash
def get_email_untrash(message_id):
    service = get_gmail_service()
    user_data2 = service.users().messages().untrash(userId='me', id=message_id).execute()
    return user_data2

#Deletes the specified message permanently
def get_email_delete(message_id):
    service = get_gmail_service()
    user_data3 = service.users().messages().delete(userId='me', id=message_id).execute()
    return user_data3

#To modify the contents
def get_email_modify(message_id):
    string = {
            "addLabelIds": [ 
                "STARRED"
            ],
            "removeLabelIds": [ 
                "CATEGORY_UPDATES"
            ],
        }
    service = get_gmail_service()
    data = service.users().messages().modify(userId='me', id=message_id, body=string).execute()
    return data

if __name__ == '__main__':
    #pprint.pprint(get_email_list())
    pprint.pprint(get_email_content('179cc454588f3ff4'))
    #pprint.pprint(get_email_trash('179a75755ad863cf'))
    #pprint.pprint(get_email_untrash('179a75755ad863cf'))
    #pprint.pprint(get_email_delete('179cc454588f3ff4'))
    #pprint.pprint(get_email_modify('179abe2bcbf78d9f'))
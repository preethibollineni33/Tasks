from __future__ import print_function
import os.path
import pytest
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
#Test method to check whether the id is in list or not
def test_get_email_list():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages=results.get('messages', [])
    lst=[label['id'] for label in messages]
    assert '179cecde8ee51eab' in lst,'Id is not present in mailbox list'

#Gets the specified message
#Test method to check whether the id content is present or not
def test_get_email_content():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages=results.get('messages', [])
    gmail_get=[label['id'] for label in messages]
    assert  len(gmail_get[0])!=0
    

#Moves the specified message to trash
#Test method to check whether the id is in trash or not
def test_get_email_trash():
    service = get_gmail_service()
    user_data1 = service.users().messages().trash(userId='me', id='179a75755ad863cf').execute()
    results=service.users().messages().list(userId='me',maxResults=10).execute()
    messages=results.get('messages',[])
    gmail_trash=[label['id']for label in messages]
    assert '179a75755ad863cf' not in gmail_trash,'Not in trash'


#Removes the specified message from the trash
#Test method to check whether the trashed id is in user's mailbox or not
def test_get_email_untrash():
    service = get_gmail_service()
    user_data2 = service.users().messages().untrash(userId='me', id='179a75755ad863cf').execute()
    results=service.users().messages().list(userId='me',maxResults=10).execute()
    messages=results.get('messages',[])
    gmail_untrash=[label['id']for label in messages]
    assert '179a75755ad863cf' not in gmail_untrash


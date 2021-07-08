from __future__ import print_function
import os.path
import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com']

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

def get_emails_list():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', maxResults=15).execute()
    return results.get('messages', [])

def get_email_content(message_id):
    #pass
    service = get_gmail_service()
    user_data = service.users().messages().get(userId='me', id=message_id).execute()
    return user_data
if __name__ == '__main__':
    '''
    messages=get_emails_list()
    for message in messages:
        print(message['id'])
    '''
    pprint.pprint(get_email_content('179a6cbc2c4521fb'))
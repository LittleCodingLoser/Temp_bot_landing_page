from __future__ import print_function

import datetime 
from datetime import datetime,timezone,timedelta
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def authorize_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
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
                'C:/Users/Weber Chang/OneDrive/桌面/temperature bot/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

def check_date():
    try:
        creds = Credentials.from_authorized_user_file('./google-credentials.json', SCOPES)
        service = build('calendar', 'v3', credentials=creds)
        # Call the Calendar API and get the current time (Taiwan)
        time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
        
        # get the event at the current hour
        events_result = service.events().list(calendarId='primary', timeMin= time[:10] + f'T{time[11:13]}:00:00+08:00',
                                              timeMax=time[:10] + f'T{time[11:13]}:15:00+08:00',
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        # 檢查是否為上課日
        if not events or events[0]['summary'] != "Working time":
            return 0
        return 1

    except Exception as error:
        print('An error occurred: %s' % error)
        return 0
authorize_google()
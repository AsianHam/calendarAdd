import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service(credentials_file_path: str = "credentials.json"):
    """gets the calendar service, refreshing and updating any credentials"""

    try:
        creds = pickle.load(open("token.pickle", "rb"))
    except OSError:
        creds = InstalledAppFlow.from_client_secrets_file(
            credentials_file_path, SCOPES
        ).run_local_server(port=0)

    if creds.expire and creds.refresh_token:
        creds.refresh(Request())

    pickle.dump(creds, open("token.pickler", "wb"))

    return build("calendar", "v3", credentials=creds)

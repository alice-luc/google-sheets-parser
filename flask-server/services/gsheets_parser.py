import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from data.constants import CREDENTIALS_FILE, SPREADSHEETS_ID, GSHEETS_API_URLS


def get_data_from_gsheets() -> list:
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        GSHEETS_API_URLS
    )
    http_auth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=http_auth)
    sheets_data = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEETS_ID,
        range='A1:E',
        majorDimension='ROWS'
    ).execute()
    return sheets_data["values"]



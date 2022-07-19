from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from data.constants import CREDENTIALS_FILE, SPREADSHEETS_ID, GSHEETS_API_URLS


def get_data_from_gsheets() -> dict:
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        GSHEETS_API_URLS
    )
    http_auth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=http_auth)
    sheets_data = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEETS_ID,
        range='A1:E',
        majorDimension='COLUMNS'
    ).execute()
    return {key[0]: key[1:] for key in sheets_data["values"]}


pprint(get_data_from_gsheets())

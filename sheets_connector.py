from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

def get_sheets_service(creds_path):
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = service_account.Credentials.from_service_account_file(creds_path, scopes=scopes)
    service = build('sheets', 'v4', credentials=credentials)
    return service

def write_to_sheet(sheet_id, range_name, values, creds_path):
    service = get_sheets_service(creds_path)
    sheet = service.spreadsheets()
    body = {'values': values}
    result = sheet.values().update(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
    return result.get('updatedCells')

def read_from_sheet(sheet_id, range_name, creds_path):
    service = get_sheets_service(creds_path)
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=range_name
    ).execute()
    return result.get('values', [])

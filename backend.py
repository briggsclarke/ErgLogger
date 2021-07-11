import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('erg-logger-9466b638613c.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Test').sheet1

wks.append_row(['10000','1:50.0','20', '0:36.00'])
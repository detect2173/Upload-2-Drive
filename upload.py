from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from datetime import *
import shutil
import os
import time

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#Upload to Google Drive
filename = date.today().strftime('%m_%d_%Y_' + 'njcc_bu.zip' )
dir_name = "C:\\xampp\\mysql\\data"
# ZIP file for upload
shutil.make_archive(filename, 'zip', dir_name)
file_metadata = {
    'name': filename ,
    'parents': ['1vlgBpmUWURZYd5TYS9K7WXHZH-ZGp_2w']
}
media_content = MediaFileUpload(filename + '.zip', mimetype='application/zip')
file = service.files().create(
    body=file_metadata,
    media_body = media_content,
).execute()







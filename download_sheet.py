import os.path
import io
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# *** CONFIGURATION ***
# Replace this with your actual File ID. 
# You can get this from the URL of your Google Sheet: https://docs.google.com/spreadsheets/d/FILE_ID_IS_HERE/edit
FILE_ID = '181U6sO_Oo4PR2Dyca8Uunt39FrkoKAy5lCSCSh4YBKo' 
# *********************

def main():
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
            if not os.path.exists('credentials.json'):
                print("ERROR: credentials.json not found. Please follow the setup guide to create it.")
                return
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    try:
        # Call the Drive v3 API
        # Get file metadata to get the name
        file_metadata = service.files().get(fileId=FILE_ID).execute()
        file_name = file_metadata.get('name')
        
        print(f"Found file: {file_name}")

        # Create 'sheets' directory if it doesn't exist
        output_dir = 'sheets'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Generate timestamped filename
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M")
        output_filename = os.path.join(output_dir, f"{file_name}_{timestamp}.xlsx")
        
        # Download the file as Excel
        request = service.files().export_media(fileId=FILE_ID, mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")

        # Save to local file
        with open(output_filename, 'wb') as f:
            f.write(fh.getvalue())
            
        print(f"Successfully saved to: {os.path.abspath(output_filename)}")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Helpful error message for 404
        if '404' in str(e):
             print("\nERROR: File not found. Please check if the FILE_ID in the script is correct and you have access to it.")

if __name__ == '__main__':
    main()

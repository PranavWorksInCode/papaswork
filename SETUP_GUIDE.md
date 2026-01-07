# Google Sheet Downloader Setup Guide

## Step 1: Get Google Cloud Credentials
To allow the script to access your Google Sheets, you need a "key" from Google.

1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Click **"Select a project"** (top left) > **"New Project"**. Name it "Sheet Downloader" and click **Create**.
3.  In the search bar at the top, type **"Google Drive API"**, select it, and click **Enable**.
4.  Click **"Credentials"** (left sidebar) > **"Create Credentials"** > **"OAuth client ID"**.
5.  If asked to configure the "Consent Screen", choose **External**, fill in the App Name ("Sheet Downloader") and your email, and click **Save**. You don't need to add scopes/test users for this personal use.
6.  Go back to **Credentials** > **Create Credentials** > **OAuth client ID**.
7.  Application type: **Desktop app**. Name: "Desktop Client". Click **Create**.
8.  Download the JSON file (click the download icon) and **rename it to `credentials.json`**.
9.  **Move `credentials.json` into this folder:** `c:\Users\asand\Desktop\papawork`.

## Step 2: Get Your File ID
1.  Open your Google Sheet in a browser.
2.  Look at the URL. It looks like this:
    `https://docs.google.com/spreadsheets/d/abc123456789.../edit`
3.  Copy the long text between `/d/` and `/edit`. That is your **File ID**.
4.  Open `download_sheet.py` in Notepad or your editor.
5.  Replace `'YOUR_FILE_ID_HERE'` with your actual File ID.

## Step 3: Install Requirements
1.  Open Command Prompt (search "cmd" in Windows start menu).
2.  Type this and press Enter:
    ```cmd
    cd /d c:\Users\asand\Desktop\papawork
    pip install -r requirements.txt
    ```

## Step 4: First Run (Authentication)
1.  Double click `run_downloader.bat`.
2.  A browser window will open asking you to sign in to Google.
3.  **Allow** the permissions.
4.  Once signed in, the script will create a `token.json` file. This means setup is complete!

## Step 5: Schedule Daily Download
1.  Double click `setup_schedule.bat`.
2.  This will create a task to run the downloader every day at **5:00 PM**.

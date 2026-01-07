# DEPLOYMENT GUIDE: How to Run on a New Computer

**Assumption:** You have already added the new user's email address to the "Test Users" list in Google Cloud Console.

## Step 1: Install Python
If the new computer doesn't have Python:
1.  Download from [python.org](https://www.python.org/downloads/).
2.  **IMPORTANT:** Check the box **"Add Python to PATH"** before clicking Install.

## Step 2: Get the Code
Open Command Prompt (cmd) on the new computer and run:
```cmd
cd Desktop
git clone https://github.com/PranavWorksInCode/papaswork.git
cd papaswork
```

## Step 3: valid secrets (CRITICAL STEP)
The file `credentials.json` is a secret key and was **NOT** uploaded to GitHub for security.
You must manually transfer it.

1.  **On your Main PC**: Copy the `credentials.json` file.
2.  **On the New PC**: Paste it into the `Desktop\papaswork` folder.

## Step 4: Install Dependencies
Open Command Prompt and navigate to the folder:
```cmd
cd Desktop\papaswork
pip install -r requirements.txt
```

## Step 5: First Run & Sign In
1.  Double-click `run_downloader.bat`.
2.  A browser will open.
3.  **Sign In** using the email address you added to the "Test Users".
4.  Since it is in Testing mode, you might see a "Google hasn't verified this app" warning. Click **Continue**.
5.  Allow access.

*Note: Once signed in, a `token.json` file is created. You won't need to sign in again.*

## Step 6: Schedule It
1.  Double-click `setup_schedule.bat`.
2.  This sets the daily timer.

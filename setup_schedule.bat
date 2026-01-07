@echo off
echo Creating scheduled task for Google Sheet Downloader...
schtasks /create /tn "Google Sheet Downloader" /tr "c:\Users\asand\Desktop\papawork\run_downloader.bat" /sc daily /st 17:00 /f
if %errorlevel% equ 0 (
    echo Task created successfully!
    echo It will run every day at 17:00 (05:00 PM).
) else (
    echo Failed to create task. You might need to run this as Administrator.
)
pause

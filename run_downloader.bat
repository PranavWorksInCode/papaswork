@echo off
cd /d "c:\Users\asand\Desktop\papawork"
python download_sheet.py
if %errorlevel% neq 0 (
    echo Error occurred during download.
    pause
)

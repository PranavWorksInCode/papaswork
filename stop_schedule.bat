@echo off
echo Stopping and Deleting the Google Sheet Downloader task...
schtasks /delete /tn "Google Sheet Downloader" /f
if %errorlevel% equ 0 (
    echo Task deleted successfully! It will no longer run automatically.
) else (
    echo Failed to delete task. It might not exist or you need Administrator privileges.
)
pause

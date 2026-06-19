@echo off
setlocal

set BOT_DIR=%~dp0
for /f "delims=" %%i in ('where python') do set PYTHON=%%i

echo Registering RCA Forum Orchestrator scheduled tasks...

schtasks /Create /TN "RCA-Reminder" /TR "\"%PYTHON%\" \"%BOT_DIR%remind.py\"" /SC WEEKLY /D MON /ST 08:00 /F
schtasks /Create /TN "RCA-Scan" /TR "\"%PYTHON%\" \"%BOT_DIR%scan.py\"" /SC DAILY /ST 09:00 /F
schtasks /Create /TN "RCA-Review" /TR "\"%PYTHON%\" \"%BOT_DIR%review.py\"" /SC DAILY /ST 10:00 /F

echo.
echo Tasks registered. Verify in Task Scheduler or run:
echo   schtasks /Query /TN "RCA-Reminder"
echo   schtasks /Query /TN "RCA-Scan"
echo   schtasks /Query /TN "RCA-Review"
echo.
echo IMPORTANT: The tasks run in the system account by default.
echo To run with your user credentials (needed for .env and Jira access),
echo open Task Scheduler, find each task, and update "Run as" to your account.

endlocal

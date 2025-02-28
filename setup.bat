@echo off

:: Check if Python is installed
where python >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

:: Check if pip is installed
where pip >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo pip is not installed. Please install pip and try again.
    pause
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv .env

:: Activate virtual environment
echo Activating virtual environment...
call .env\Scripts\activate

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup complete! Run the app using:
echo   python run.py
pause

@echo off
echo Making virtual environment...
python -m venv .venv

echo Entering virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Installing Flask inside venv...
pip install flask

echo.
echo Initializing database...
python backend/debug.py events

echo.
echo Opening website URL...
start http://127.0.0.1:5000

echo.
echo Starting website server...
python backend\app.py

pause

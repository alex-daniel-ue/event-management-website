@echo off
echo Making virtual environment (.venv)...
python -m venv .venv

echo Entering virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Installing Flask inside virtual environment...
pip install flask

echo.
echo Initializing database...
python backend/initialize_db.py

echo.
echo Opening website URL...
start http://127.0.0.1:5000

echo.
echo Starting website server...
python backend\app.py

pause

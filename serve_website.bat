@echo off
call .venv\Scripts\activate.bat
start http://127.0.0.1:5000
python backend\app.py
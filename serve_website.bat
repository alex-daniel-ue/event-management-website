@echo off
python -m venv .venv
pip install flask
call .venv\Scripts\activate.bat
start http://127.0.0.1:5000
python backend\app.py
pause
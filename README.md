# Event Management Website[^1]
[^1]: kailangan na naten ng pangalan frfr

## Tech stack
### Backend
- Python
- Flask (Web framework)
- SQLite (Database)
### Frontend
- HTML, CSS, JS
- Jinja (Template engine)

## Requirements
- Python 3.12
- pip (Python package manager)

## Setup
1. Clone or download the repository ![Code > Download ZIP, or use Git](https://i.ibb.co/rKHRwYcv/tutorial.png) 
2. Run `serve_website.bat`
3. Enjoy

## Extra info
### Jinja
Same lang siya sa Python syntax, need siya para mapakita dynamically yung each event.
Check niyo [dito](https://documentation.bloomreach.com/engagement/docs/jinja-syntax) for more info.

### Debugging & testing
- Para ma-view lahat ng records sa `events` table:
```
python backend/debug_db.py events
```
- Para matanggal lahat ng entries sa `events` table:
```
python backend/debug_db.py events --reset
```

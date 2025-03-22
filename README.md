# Event Management Website[^1]
[^1]: kailangan na naten ng pangalan frfr

## Tech stack
### Backend
- Python
- Flask (Web framework)
- SQLite (Database)
### Frontend
- HTML, CSS, JS
- Jinja2 (Template engine)

## Setup
1. Clone or download the repository ![Code > Download ZIP, or use Git](https://i.ibb.co/rKHRwYcv/tutorial.png) 
2. Run `serve_website.bat`
3. Enjoy

## Extra info
### Jinja2
Same lang siya sa Python syntax, need siya para mapakita dynamically yung each event.
Check niyo [dito](https://documentation.bloomreach.com/engagement/docs/jinja-syntax) for more info.

### Debugging & testing
Run niyo to sa CLI para ma-initialize yung `events.db`, assuming directory niyo nasa `event-management-website/`:
`python backend/debug.py`

Para matanggal lahat ng entries sa database:
`python backend/debug.py --reset`

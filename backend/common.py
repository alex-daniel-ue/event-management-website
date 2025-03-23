import functools
import sqlite3
import os

EVENTS_DB_PATH = os.path.join(os.path.dirname(__file__), "events.db")

def get_database(path: str):
    return sqlite3.connect(path)

def events(func):
    """Decorator that manages database connection and cursor for the wrapped function.
    
    Establishes a connection to the database, creates a cursor, and closes both after the function executes.
    Use events.connection and events.cursor for SQLite3 operations.
    """

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        events.connection = get_database(EVENTS_DB_PATH)
        events.cursor = events.connection.cursor()
        result = func(*args, **kwargs)

        events.cursor.close()
        events.connection.close()
        return result
    
    return decorated
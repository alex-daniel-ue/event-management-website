import contextlib
import sqlite3
import os

DATABASE_FILE_NAME = "database.db"

@contextlib.contextmanager
def get_cursor():
    db_path = os.path.join(os.path.dirname(__file__), DATABASE_FILE_NAME)
    connection = sqlite3.connect(db_path)
    try:
        cursor = connection.cursor()
        yield cursor
        connection.commit()
    except:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()
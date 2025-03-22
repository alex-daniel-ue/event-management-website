"""
debug.py

This module provides debugging and testing functions for the 'events' table. 

Functions:
- initialize: Creates the 'events' table if it doesn't exist.
- reset: Drops the 'events' table.
- view_all: Retrieves and prints all records from the 'events' table. If the table is empty,
  it notifies the user.

Usage:
Run this module as a standalone script, using CLI. For example:
    python backend/debug.py
If the -r or --reset flag is provided, it will execute reset().
Then it will execute initialize() then view_all().
"""

import argparse
from common import *


@events
def initialize() -> None:
    events.cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_added DATETIME NOT NULL
        );
    """)
    events.connection.commit()

@events
def reset() -> None:
    events.cursor.execute("DROP TABLE events;")
    events.connection.commit()

@events
def view_all() -> None:
    records = events.cursor.execute("SELECT * FROM events;").fetchall()
    if records:
        print(*records, sep='\n')
    else:
        print("The 'events' table is empty.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reset", action="store_true")
    flags = parser.parse_args()

    if flags.reset:
        reset()
        print("Reset 'events' table.")
    initialize()
    view_all()
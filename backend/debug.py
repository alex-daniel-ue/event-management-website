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

If the -r or --reset flag is appended, it will execute reset().
    python backend/debug.py --reset

Then it will execute initialize() then view_all().
"""

import argparse
from common import *


def declare_tables() -> None:
    with get_cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_added DATETIME NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
            );
        """)


def reset_table(table_name) -> None:
    with get_cursor() as cursor:
        cursor.execute(f"DROP TABLE {table_name};")


def select_all(table_name) -> None:
    with get_cursor() as cursor:
        records = cursor.execute(f"SELECT * FROM {table_name}").fetchall()

    if records:
        return "\n".join(repr(record) for record in records)
    return f"The '{table_name}' table is empty."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("table_name", help="The name of the table to be viewed or reset")
    parser.add_argument("-r", "--reset", action="store_true", help="The flag that indicates whether the table will be reset")
    args = parser.parse_args()

    if args.reset:
        reset_table(args.table_name)
        print(f"Reset '{args.table_name}' table.")
    declare_tables()
    print(select_all(args.table_name))

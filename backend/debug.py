"""
debug.py

This module provides debugging and testing functions for the 'events' table in the SQLite database.

Functions:
- initialize: Creates the 'events' and 'users' tables if they do not exist.
- reset_table: Drops the specified table from the database.
- select_all: Retrieves and prints all records from the specified table. If the table is empty, it notifies the user.

Usage:
Run this module as a standalone script using the command line interface (CLI). For example:
    python backend/debug.py <table_name>

If the -r or --reset flag is appended, it will execute reset_table() for the specified table.
    python backend/debug.py <table_name> --reset

After resetting, it will execute initialize() and then select_all() to display the current records in the table.

Parameters:
- table_name (str): The name of the table to be viewed or reset.
- -r, --reset (optional): A flag indicating whether the specified table should be reset.
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
                name TEXT NOT NULL
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

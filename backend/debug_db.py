"""
debug_db.py

Usage:
    python debug_db.py <table_name> [-r|--reset]

Arguments:
    table_name    Name of the database table to view or reset

Options:
    -r, --reset   Reset (drop and re-initialize) the specified table before viewing

Examples:
    # View all records in the 'events' table
    python script.py events
    
    # Reset and then view the 'events' table
    python script.py events --reset
"""

import argparse
from initialize_db import *
from common import *


def reset_table(table_name) -> None:
    with get_cursor() as cursor:
        cursor.execute(f"DROP TABLE {table_name};")
    declare_tables()

def select_all(table_name) -> None:
    with get_cursor() as cursor:
        records = cursor.execute(f"SELECT * FROM {table_name}").fetchall()

    if records:
        return "\n".join(repr(record) for record in records)
    return f"The '{table_name}' table is empty."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("table_name", help="The target table's name")
    parser.add_argument("-r", "--reset", action="store_true", help="The flag indicating whether target table will be reset")
    args = parser.parse_args()

    if args.reset:
        reset_table(args.table_name)
        print(f"Reset '{args.table_name}' table.")
    print(select_all(args.table_name))

from common import *


# TODO: Does CRUD need to be in Event?
class Event:
    # __slots__ restricts the possible class variables, improving memory usage
    __slots__ = ("id", "name", "date_added")

    def __init__(self, id: int, name: str, date_added: str) -> None:
        """This serves to ease front-end development, allowing dot notation like "event.name" or "event.date_added" in Jinja.
        Without this, they have to use bracket notation ("event[1]" or "event["name"]").
        """

        self.id = id
        self.name = name
        self.date_added = date_added
        # TODO: Add more class variables (location, ticket_price, venue_capacity, etc.)


    @staticmethod
    def create(name: str) -> None:
        with get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO events (name, date_added)
                VALUES (?, CURRENT_TIMESTAMP);
            """, (name,)
            )
    

    @staticmethod
    def read(filter: str = None, *values, limit: tuple = None) -> list:
        # TODO: Add table_name argument
        query = f"SELECT id, name, date_added FROM events"

        if filter is not None:
            query += f" WHERE {filter}"
        
        if limit is not None:
            if (1 <= len(limit) <= 2) and all(isinstance(n, int) for n in limit):
                query += f" LIMIT {','.join(map(str, limit))}" 
            else:
                raise ValueError("LIMIT keyword should have 1-2 ints: (LENGTH) or (OFFSET,LENGTH).")
        
        with get_cursor() as cursor: 
            records = cursor.execute(query, values).fetchall()
        
        # TODO: Change this when implemented users table
        return [Event(*record) for record in records]


    @staticmethod
    def update(id: int, **attributes_to_values) -> None:
        # TODO: Replace id argument with filter argument, as that is more versatile
        attributes = [f"{attribute} = ?" for attribute in attributes_to_values.keys()]
        values = attributes_to_values.values()

        with get_cursor() as cursor:
            cursor.execute(f"""
                UPDATE events SET {', '.join(attributes)}
                WHERE id = ?
            """, (*values, id)
            )


    @staticmethod
    def delete(id: int) -> None:
        # TODO: Replace this entirely with filter or better SQL query.
        with get_cursor() as cursor:
            cursor.execute("""
                DELETE FROM events WHERE id = ?
            """, (id,)
            )

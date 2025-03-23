from common import *

class Event:
    # __slots__ restricts the possible class variables, improving memory usage
    __slots__ = ("id", "name", "date_added")
    def __init__(self, id: int, name: str, date_added: str) -> None:
        """
        This serves to ease front-end development, letting them reference the actual attributes like 'event.name' or 'event.date_added' in Jinja2.
        Otherwise, without this, they have to write 'event[1]' or 'event[2]' respectively.
        """
        self.id = id
        self.name = name
        self.date_added = date_added
        #TODO: Add more class variables (location, ticket_price, capacity, etc.)

    @staticmethod
    @events
    def create(name: str) -> None:
        events.cursor.execute("INSERT INTO events (name, date_added) VALUES (?, CURRENT_TIMESTAMP);", (name,))
        events.connection.commit()
    
    @staticmethod
    @events
    def select_all() -> tuple:
        records = events.cursor.execute("SELECT * FROM events;").fetchall()
        # Initializes an Event object for each record
        return (Event(*record) for record in records)

    @staticmethod
    @events
    def delete(id: int):
        events.cursor.execute("DELETE FROM events WHERE id = ?", (id,))
        events.connection.commit()

    #TODO: def update() or edit():
    #TODO: def delete():
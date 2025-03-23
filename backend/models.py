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
        # TODO: Add more class variables (location, ticket_price, venue_capacity, etc.)


    @staticmethod
    @events
    def create(name: str) -> None:
        events.cursor.execute("INSERT INTO events (name, date_added) VALUES (?, CURRENT_TIMESTAMP);", (name,))
        events.connection.commit()
    

    @staticmethod
    @events
    def read(filter: str = "", *values) -> list:
        command = "SELECT id, name, date_added FROM events"
        if filter:
            command = f"{command} WHERE {filter}"

        records = events.cursor.execute(command, values).fetchall()
        return [Event(*record) for record in records]


    @staticmethod
    @events
    def update(id: int, **attributes_to_values) -> None:
        """ Here, attributes_to_values shows in function calls as name="New Event Name" or price=1500 """
        # TODO: Replace id argument with filter argument, as that is more versatile
        # TODO: Also replace for loop with one better SQL query.
        for attribute, value in attributes_to_values.items():
            events.cursor.execute(f"UPDATE events SET {attribute} = ? WHERE id = ?", (value, id))
        events.connection.commit()


    @staticmethod
    @events
    def delete(id: int) -> None:
        # TODO: Replace this entirely with filter or better SQL command.
        events.cursor.execute("DELETE FROM events WHERE id = ?", (id,))
        events.connection.commit()

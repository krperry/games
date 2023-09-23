"""Class to contain the room information"""
from unit import Unit

1


class Room(Unit):
    """
    This class defines the room type dirived from Unit
    """

    def __init__(self, location, title, desc):
        """Constructor"""
        super().__init__([], title, desc)
        self.location = location
        self.exits = {"north": None, "east": None, "south": None, "west": None}
        self.items = None

    def set_direction(self, direction, location):
        """Set the location this a given exit leads to"""
        self.exits[direction] = location

    def add_item(self, item):
        """Add an item to this rooms contents"""
        if not self.items:
            self.items = []
        self.items.append(item)

    def get_item(self, name):
        """get an item from this room by given name"""
        i = self.items[name]
        del self.items[name]
        return i

    def get_room_string(self):
        """Get rooms full description"""
        return (
            f"{self.title}\n{self.description}\n"
            + f"You can walk {self.directions()}\n{self.get_items_string()}\n"
        )

    def directions(self):
        """return direction string"""
        dir_str = ""
        for direction, room in self.exits.items():
            if room != None:
                dir_str += direction + ", "
        return f"[{dir_str.strip().strip(',')}]"

    def has_exit(self, direction):
        """Returns if this room has a given exit"""
        return self.exits[direction]

    def get_items_string(self):
        """Gets description of items in the room"""
        if not self.items:
            return ""
        for item in self.items:
            item_str = item.get_title() + "is laying on the ground.\n"
        return item_str

    def remove_item(self, item):
        """Remove this item from room"""
        if not self.items:
            return None
        for i in range(len(self.items)):
            if self.items[i].is_name(item):
                tItem = self.items[i]
                del self.items[i]
                if len(self.items) < 1:
                    self.items = None
                    return tItem
        return None

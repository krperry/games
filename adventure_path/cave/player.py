"""Player information class""" "cave.lnt"

from unit import Unit


class Player(Unit):
    """

    This class defines the basic Player.
    """

    def __init__(self, n, t, d):
        """Constructor"""

        super().__init__(n, t, d)

        self.health = 8

        self.location = None

        self.items = None

    def can_move(self, direction):
        """Checks if player can move."""
        return self.location.has_exit(direction)

    def set_location(self, room):
        """Sets the room player is in"""
        self.location = room

    def get_location(self):
        """Get player current location"""
        return self.location

    def get_health(self):
        """REturn current health"""

        return self.health

    def lose_health(self):
        """decrease health by one"""

        self.health -= 1

        return self.health

    def move(self, direction):
        """move player in a direction"""
        self.location = self.location.exits[direction]

        print("You move ", direction)

        print(self.location.get_room_string())

    def add_item(self, item):
        """Adds an item to players inventory"""
        if not self.items:
            self.items = []
        if item:
            self.items.append(item)

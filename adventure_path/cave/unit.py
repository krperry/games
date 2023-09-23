"""Base class for player, room, and item"""


class Unit:
    """
    This class defines the basic Unit.
    """

    def __init__(self, name, title, desc):
        """Constructor"""
        self.names = name
        self.title = title
        self.description = desc

    def is_name(self, name):
        """tests if this is the units name"""
        if name in self.names:
            return True
        return False

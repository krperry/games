"""Item class for Cave game"""
from unit import Unit


class Item(Unit):
    """
    This class defines the basic item.
    """

    def __init__(self, n, t, d, c):
        """Constructor"""
        super().__init__(n, t, d)
        self.cost = c

    def get_title(self):
        """Return the title for this item"""
        return self.title

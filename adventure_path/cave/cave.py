"""All the Cave room definitions rooms and items"""
import time
import random

import sys


from room import Room

from player import Player

from item import Item

random.seed(time.time())


rooms = [
    Room(
        "cave0",
        "Dark Tunnel",
        """

This is a dark dank tunnel of a cave.
""",
    ),
    Room(
        "cave1",
        "Dark Northeast Corner",
        """

This is a dark dank corner of the cave
""",
    ),
    Room(
        "cave2",
        "Dark North side",
        """

This is a dark dank side of the cave
""",
    ),
    Room(
        "cave3",
        "Dark Northwest Corner",
        """

This is a dark dank corner of the cave
""",
    ),
    Room(
        "cave4",
        "Dark West side",
        """

This is a dark dank side of the cave
""",
    ),
    Room(
        "cave5",
        "Dark center",
        """

This is the  dark dank center of the cave.  It is impossible to see in any direction.
""",
    ),
    Room(
        "cave6",
        "Dark east side",
        """

This is a dark dank side of the cave
""",
    ),
    Room(
        "cave7",
        "Dark Southwest Corner",
        """

This is a dark dank corner of the cave
""",
    ),
    Room(
        "cave8",
        "Dark Entrance",
        """

This is a dark dank entrance of the cave
""",
    ),
    Room(
        "cave9",
        "Dark SoutheastCorner",
        """

This is a dark dank corner of the cave
""",
    ),
]


# Setup layout

# cave1 exits
rooms[1].set_direction("east", rooms[2])
rooms[1].set_direction("south", rooms[4])

# room 2 exits
rooms[2].set_direction("east", rooms[3])
rooms[2].set_direction("south", rooms[5])
rooms[2].set_direction("west", rooms[1])

# room 3 exits
rooms[3].set_direction("west", rooms[2])
rooms[3].set_direction("south", rooms[6])

# cave4 exits
rooms[4].set_direction("east", rooms[5])
rooms[4].set_direction("south", rooms[7])
rooms[4].set_direction("north", rooms[1])

# room 5 exits
rooms[5].set_direction("north", rooms[2])
rooms[5].set_direction("east", rooms[6])
rooms[5].set_direction("south", rooms[8])
rooms[5].set_direction("west", rooms[4])

# room 6 exits
rooms[6].set_direction("north", rooms[3])
rooms[6].set_direction("west", rooms[5])
rooms[6].set_direction("south", rooms[9])

# cave7 exits
rooms[7].set_direction("north", rooms[4])
rooms[7].set_direction("east", rooms[8])

# room 8 exits
rooms[8].set_direction("north", rooms[5])
rooms[8].set_direction("east", rooms[9])
rooms[8].set_direction("south", rooms[0])
rooms[8].set_direction("west", rooms[7])

# room 9 exits
rooms[9].set_direction("north", rooms[6])
rooms[9].set_direction("west", rooms[8])

# room 0 exits
rooms[0].set_direction("north", rooms[8])

# place player in cave 0

player = Player("Milo", "an old man", "A short old man he is.")

player.set_location(rooms[0])


# make item to find

item = Item(
    [
        "little gold box",
        "little gold",
        "little box",
        "Gold box",
        "little",
        "gold",
        "box",
    ],
    "a little Gold box",
    """

This looks like the little gold box you were looking for.  Now pick it up and run for the way out.
    """,
    100,
)

# place item randomly

randRooms = [1, 2, 3, 4, 6, 7, 9]

i = random.randint(0, 6)

rooms[randRooms[i]].add_item(item)


# run game.


def do_get(cmd, args):
    """

    This is the get function that will let players pick up items.
    """

    take_item = player.get_location().remove_item(args)

    if not take_item:
        print(f"No {args} found.")

    else:
        player.add_item(take_item)

        print(f"You pick up {take_item.get_title()}.")


def get_long_command(cmd):
    """get the long version of a short command"""

    for command in commands:
        if cmd == command[: len(cmd)]:
            return command
    return cmd


def command_args(input_string):
    """normalize function calls.  There might be a better way to do this"""

    args = input_string.split(" ", 1)

    if len(args) < 2:
        args.append("")

    try:
        args[0] = get_long_command(args[0])

        # return a 3 part tupple             function, cmd, and args

        return (commands[args[0]], args[0], args[1])

    except:
        return None


def check_win():
    """Check for a winner and kill the person if they lose"""

    if player.health < 1 and not player.items:
        print(
            "You are too tired to go on! You collapse."
            + "A big hairy Grue shows up and eats you.  Your dead."
        )

        print("Better luck next time.")

        print("Game Over.")

        sys.exit()

    if player.health < 1 and player.get_location() == rooms[0] and player.items:
        print("that was a close one!")

        print("You barely stagger into the safe room and pass out.")

        print("Your a winner!")

        print("Game over.")

        sys.exit()

    if player.get_location() == rooms[0] and player.items:
        print("Great Job!")

        print("You made it with energy to spare!")

        print("You are a master finder.")

        print("Game over.")

        sys.exit()


def do_move(cmd, args):
    """

    This moves the character and takes the health it uses
    """
    if player.can_move(cmd):
        player.move(cmd)

        player.lose_health()

        check_win()

    else:
        print("You can't go that way")


commands = {
    "get": do_get,
    "north": do_move,
    "east": do_move,
    "south": do_move,
    "west": do_move,
}


def main():
    """Main run functio of the game."""

    print("Welcome to the dark caves of the Golden box")

    print("In this cave lies a golden box")

    print("You have 9 health points to retrieve the box")

    print("You lose one health for every room you visit.")
    print(
        "If you run out of health."
        + "ou will no longer be able to move and will most certainly be eatten by a grue"
    )

    print("Return to the starting room before you run out of health.")

    print("If you find the Golden box you can take it")

    print("each room has the listed directions you can go")

    print("Good luck adventurer.")

    print(player.get_location().get_room_string())

    command = "start"

    while command not in "quit":
        command = input("enter a command >")

        targs = command_args(command)

        if targs:
            targs[0](targs[1], targs[2])

        else:
            print("No such command.")


if __name__ == "__main__":
    main()

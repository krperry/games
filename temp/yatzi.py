import random

class YatziGame:
    def __init__(self):
        self.total_score = 0
        self.dice = [0] * 5
        self.categories = [
            "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
            "Three of a Kind", "Four of a Kind", "Full House",
            "Small Straight", "Large Straight", "Yatzi", "Chance"
        ]

    def roll_dice(self):
        """Rolls five dice and stores the values in the dice attribute."""
        self.dice = [random.randint(1, 6) for _ in range(5)]

    def display_dice(self):
        """Displays the current values of the dice."""
        print("Dice:", self.dice)

    def get_dice_to_reroll(self):
        """
        Prompts the user to input the indexes of dice to reroll.
        Rerolls the selected dice, keeping the rest unchanged.
        """
        reroll = input("Enter the indexes of dice to reroll (comma-separated, 1-indexed), or enter to keep all: ")
        if reroll:
            reroll_indexes = [int(index) - 1 for index in reroll.split(",")]
            # Reroll the selected dice
            self.dice = [random.randint(1, 6) if i in reroll_indexes else die for i, die in enumerate(self.dice)]

    def calculate_score(self, category):
        """
        Calculates the score for the given category based on the current dice values.

        Args:
            category (str): The selected scoring category.

        Returns:
            int: The calculated score for the category.
        """
        def is_full_house():
            """Checks if the dice values form a Full House."""
            return len(set(self.dice)) == 2 and (self.dice.count(self.dice[0]) == 3 or self.dice.count(self.dice[0]) == 2)

        def is_small_straight():
            """Checks if the dice values form a Small Straight."""
            return set(self.dice) in ({1, 2, 3, 4, 5}, {2, 3, 4, 5, 6})

        def is_large_straight():
            """Checks if the dice values form a Large Straight."""
            return set(self.dice) in ({1, 2, 3, 4, 5}, {2, 3, 4, 5, 6})
        
        upper_section = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
        if category in upper_section:
            numeric_value = upper_section.index(category) + 1
            count = 0
            for die in self.dice:
                if die == numeric_value:
                    count += 1
            return count * numeric_value
        elif category in ["Three of a Kind", "Four of a Kind"]:
            return sum(self.dice) if any(self.dice.count(value) >= int(category.split()[-1]) for value in set(self.dice)) else 0
        elif category == "Full House" and is_full_house():
            return 25
        elif category == "Small Straight" and is_small_straight():
            return 30
        elif category == "Large Straight" and is_large_straight():
            return 40
        elif category == "Yatzi" and len(set(self.dice)) == 1:
            return 50
        elif category == "Chance":
            return sum(self.dice)
        else:
            return 0

    def play_round(self):
        """Plays a round of the Yatzi game."""
        self.roll_dice()
        self.display_dice()

        self.get_dice_to_reroll()
        self.display_dice()

        print("Available Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")

        while True:
            try:
                selected_category = int(input("Enter the number of the category to score: "))
                if 1 <= selected_category <= len(self.categories):
                    break
                else:
                    print("Invalid category number. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        category = self.categories[selected_category - 1]
        round_score = self.calculate_score(category)
        print(f"Scored {round_score} points for {category}!")

        self.total_score += round_score

    def play_game(self):
        """Plays the entire Yatzi game, consisting of 13 rounds."""
        for _ in range(13):
            self.play_round()

        print("Game Over! Total Score:", self.total_score)

if __name__ == "__main__":
    yatzi_game = YatziGame()
    yatzi_game.play_game()
    
    
    

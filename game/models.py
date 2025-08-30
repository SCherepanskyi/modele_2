import random
from game.exceptions import InvalidRollError

class BasePlayer:
    """Base class for players."""

    def __init__(self, name):
        self._name = name
        self.__score = 0

    @property
    def name(self):
        """Return the name of the player."""
        return self._name

    @property
    def score(self):
        """Return the score of the player."""
        return self.__score

    def update_score(self, points):
        """Update the score of the player."""
        self.__score += points

    def reset_score(self):
        """Reset the score of the player."""
        self.__score = 0

    @staticmethod
    def _generate_roll():
        """Generate a random number between 1 and 6."""
        return random.randint(1, 6)


class Player(BasePlayer):
    """Class for players."""

    def roll(self):
        """Player rolls a dice."""
        try:
            while True:
                user_input = input("Press Enter to roll the dice...")
                if user_input == "":
                    return self._generate_roll()
                print("Please press Enter to roll the dice.")
        except Exception as e:
            raise InvalidRollError(f"Error rolling dice: {e}")

class Computer(BasePlayer):
    """Class for computer players."""

    def __init__(self):
        super().__init__("Computer")

    def roll(self):
        """Computer rolls a dice."""
        return self._generate_roll()
from pathlib import Path

class GameSettings:
    """A class to store all settings"""

    _BASE_DIR = Path(__file__).resolve().parent.parent
    _RESULTS_FILE = _BASE_DIR / "results.json"

    _GAME_LEVEL = {
        "1": 5,
        "2": 8,
        "3": 10
    }

    _GAME_LEVELS_CONVERT = {
        5: "Short",
        8: "Medium",
        10: "Long"
    }

    _DICE_SYMBOLS = {
        1: """
            ┌─────────┐
            │         │
            │    ●    │
            │         │
            └─────────┘
            """,

        2: """
            ┌─────────┐
            │ ●       │
            │         │
            │       ● │
            └─────────┘
            """,

        3: """
            ┌─────────┐
            │ ●       │
            │    ●    │
            │       ● │
            └─────────┘
            """,

        4: """
            ┌─────────┐
            │ ●     ● │
            │         │
            │ ●     ● │
            └─────────┘
            """,

        5: """
            ┌─────────┐
            │ ●     ● │
            │    ●    │
            │ ●     ● │
            └─────────┘
            """,

        6: """
            ┌─────────┐
            │ ●     ● │
            │ ●     ● │
            │ ●     ● │
            └─────────┘
            """
    }

    @classmethod
    def get_results_file(cls):
        """Get the path to the results file"""
        return cls._RESULTS_FILE

    @classmethod
    def get_game_level(cls, level):
        """Get the game level"""
        return cls._GAME_LEVEL[level]

    @classmethod
    def get_game_level_convert(cls, level):
        """Get the game level in a readable format"""
        return cls._GAME_LEVELS_CONVERT[level]

    @classmethod
    def get_dice_symbol(cls, number):
        """Get the dice symbol"""
        return cls._DICE_SYMBOLS[number]

    @classmethod
    def validate_level_input(cls, choice):
        """Validate the level input"""
        return choice in cls._GAME_LEVEL.keys()
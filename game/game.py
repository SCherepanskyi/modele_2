import time
from datetime import datetime
from game.models import Player, Computer
from game.score import ScoreManager
from game.settings import GameSettings
from game.exceptions import InvalidInputError

class GameLogic:
    """Game logic"""

    def __init__(self):
        self._player = None
        self._computer = Computer()
        self._total_rounds = 0
        self._start_time = None
        self._current_round = 0

    @property
    def player_name(self):
        """Return the name of the player."""
        return self._player.name if self._player else None

    @property
    def player_score(self):
        """Return the score of the player."""
        return self._player.score if self._player else 0

    @property
    def computer_score(self):
        """Return the score of the computer."""
        return self._computer.score if self._computer else 0

    def start(self):
        """Start the game"""
        try:
            self._setup_game()
            self._play_game()
            self._finish_game()

        except KeyboardInterrupt:
            print("Game interrupted.")
        except Exception as e:
            print(f"Error starting game: {e}")

    def _setup_game(self):
        """Setup the game"""
        player_name = self._get_player_name()
        self._player = Player(player_name)
        self._total_rounds = self._get_game_level()
        self._start_time = datetime.now()

        self._print_game_info()

    def _play_game(self):
        """Start playing the game"""
        for round_num in range(1, self._total_rounds + 1):
            self._current_round = round_num
            self._play_round(round_num)
            time.sleep(1)

    def _finish_game(self):
        """Finish the game"""
        self._show_final_results()
        ScoreManager.save_result(
            self._player.name,
            self._total_rounds,
            self._player.score
        )

    def _get_player_name(self):
        """Set the name of the player"""
        while True:
            name = input("Enter your name: ").strip()
            if name:
                return name
            print("Name cannot be empty.")

    @staticmethod
    def _get_game_level():
        """Get the level of the game"""
        print("Choose the level of the game:")
        print("1. Short game (5 rounds)")
        print("2. Medium game (8 rounds)")
        print("3. Long game (10 rounds)")

        while True:
            choice = input("Enter the level of the game (1-3): ").strip()
            if GameSettings.validate_level_input(choice):
                return GameSettings.get_game_levels(choice)
            print("Wrong choice. Please enter 1, 2, or 3.")

    def _play_round(self, round_num):
        """Play a round of the game"""

        print(f"Round {round_num}:")

        player_roll = self._player.roll()
        computer_roll = self._computer.roll()

        self._display_roll_results(player_roll, computer_roll)
        self._process_round_result(player_roll, computer_roll)

    def _display_roll_results(self, player_roll, computer_roll):
        """Display the results of the roll"""
        player_symbol = GameSettings.get_dice_symbol(player_roll)
        computer_symbol = GameSettings.get_dice_symbol(computer_roll)

        print(f"You rolled: {player_symbol}")
        print(f"Computer rolled: {computer_symbol}")

    def _process_round_result(self, player_roll, computer_roll):
        """Process the result of the round"""

        difference = player_roll - computer_roll

        if difference > 0:
            print("You win!")
            print(f"You got +{difference} points.")
            self._player.update_score(difference)
            print(f"Current score: {self._player.score}")

        elif difference < 0:
            print("You lose!")
            print(f"You lost {difference} points.")
            self._player.update_score(difference)
            print(f"Current score: {self._player.score}")
        else:
            print("It's a tie!")
            self._play_round(self._current_round)

    def _print_game_info(self):
        """Print game information"""
        print(f"Let's start the game!")
        print(f"Player: {self._player.name}")
        print(f"Level: {self._total_rounds} rounds")
        print(f"Time started: {self._start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)

    def _show_final_results(self):
        """Show final results of the game"""
        print("\n" + "=" * 50)
        print("Game over!")
        print("=" * 50)
        print(f"Start time: {self._start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Player: {self._player.name}")
        print(f"Level: {GameSettings.get_game_level_convert(self._total_rounds)}")
        print(f"Final score: {self._player.score:+}")

        self._print_winner_message()
        print("=" * 50)

    def _print_winner_message(self):
        """Print the winner message"""
        if self._player.score > 0:
            print("You won the game!")
        elif self._player.score < 0:
            print("You lost the game!")
        else:
            print("It's a tie!")

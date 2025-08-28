from game.game import Game
from game.score import ScoreManager
import sys

class Main:
    @staticmethod
    def show_menu():
        """Show the main menu."""
        print("Welcome to the game Dice!")
        print("Press 1 to play.")
        print("Press 2 to view results.")
        print("Press 3 to quit.")

    @staticmethod
    def game_run():
        """Run the game."""
        game = Game()
        while True:
            Main.show_menu()
            choice = input("Enter your choice (1, 2, or 3): ").strip()
            if choice == "1":
                game.start()
            elif choice == "2":
                ScoreManager.show_results()
            elif choice == "3":
                print("Thanks for playing!")
                sys.exit()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    Main.game_run()
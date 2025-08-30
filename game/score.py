import json
from datetime import datetime
from game.settings import GameSettings
from game.exceptions import FileOperationError


class ScoreManager:
    """Manages game results"""

    _results_file = GameSettings.get_results_file()

    @classmethod
    def save_result(cls, name, rounds, score):
        """Save game result to file"""
        try:
            result = cls._create_result_dict(name, rounds, score)
            results = cls._load_existing_results()
            results.append(result)
            cls._save_results_to_file(results)

        except Exception as e:
            raise FileOperationError(f"Error saving results: {e}")

    @classmethod
    def display_results(cls):
        """Display game results"""
        try:
            results = cls._load_existing_results()
            cls._print_results(results)

        except FileOperationError:
            print("There are no saved results.")
        except Exception as e:
            print(f"Error reading results: {e}")

    @staticmethod
    def _create_result_dict(name, rounds, score):
        """Create a dictionary with game result data"""
        return {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Player": name,
            "Number of rounds": rounds,
            "Total score": score
        }

    @classmethod
    def _load_existing_results(cls):
        """Load existing game results from file"""
        if not cls._results_file.exists():
            return []

        try:
            with open(cls._results_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    @classmethod
    def _save_results_to_file(cls, results):
        """Save game results to file"""
        with open(cls._results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

    @staticmethod
    def _print_results(results):
        """Display game results in console"""
        if not results:
            print("There are no saved results.")
            return

        print("Results of previous games:")
        print("-" * 50)

        for result in results:
            print(f"Date: {result['Date']}")
            print(f"Player: {result['Player']}")
            print(f"Number of rounds : {result['Number of rounds']}")
            print(f"Total score: {result['Total score']:+}")
            print("-" * 50)
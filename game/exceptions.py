class GameError(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidInputError(GameError):
    """Exception raised for errors in the input."""
    pass


class InvalidRollError(GameError):
    """Exception raised for errors in roll of dice."""
    pass


class FileOperationError(GameError):
    """Exception raised for errors in file operation."""
    pass

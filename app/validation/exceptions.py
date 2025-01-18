class InvalidInputError(Exception):
    """Exception raised when the user input is invalid."""

    def __init__(self, message: str):
        super().__init__(message)


class ConfigurationError(Exception):
    """Exception raised when there is a configuration error."""

    def __init__(self, message: str):
        super().__init__(message)

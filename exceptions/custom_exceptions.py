# exceptions/custom_exceptions.py

class LocatorNotFoundException(Exception):
    """Raised when a required locator is not found."""

    def __init__(self, message = "Locator not found"):
        self.message = message
        super().__init__(self.message)


class SortingFailedException(Exception):
    """Raised when sorting fails to reach the expected state."""

    def __init__(self, message="Sorting failed"):
        self.message = message
        super().__init__(self.message)


class DownloadFailedException(Exception):
    """Raised when the download of a file fails."""

    def __init__(self, message="Download failed"):
        self.message = message
        super().__init__(self.message)


class FileSaveException(Exception):
    """Raised when saving the downloaded file fails."""

    def __init__(self, filepath, message="Failed to save the file"):
        self.filepath = filepath
        self.message = f"{message}: {filepath}"
        super().__init__(self.message)



class SliderValueNotReachedException(Exception):
    def __init__(self, message):
        super().__init__(message)

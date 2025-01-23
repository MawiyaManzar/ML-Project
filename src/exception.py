from src.logger import logging
import sys

def error_message_detail(error, error_detail: sys):
    """Generate a detailed error message.

    This function extracts the file name and line number where the error occurred,
    and formats them into a detailed error message.
    """
    # Extract traceback information
    _, _, exc_tb = error_detail.exc_info()
    # Get the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Format the error message with file name, line number, and error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    """Custom exception class for detailed error messages."""

    def __init__(self, error_message, error_detail: sys):
        """Initialize the custom exception with a detailed error message."""
        super().__init__(error_message)
        # Generate a detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """Return the detailed error message when the exception is printed."""
        return self.error_message
    


        
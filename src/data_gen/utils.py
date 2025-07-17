# utils.py: Utility functions and configurations shared across the package.
# Currently includes logging setup; can be expanded for other helpers.

import logging

logging.basicConfig(level=logging.INFO)  # Set logging level to INFO for standard output.

def log_info(message: str):
    """
    Log an informational message.

    Parameters:
    - message (str): The message to log.
    """
    logging.info(message)  # Use logging module to output info.
import logging
import os
from logging.handlers import RotatingFileHandler

# Define the log directory and file
LOG_DIR = "logs"
LOG_FILE = "app.log"

# Create the log directory if it does not exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure the logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = RotatingFileHandler(os.path.join(LOG_DIR, LOG_FILE), maxBytes=5 * 1024 * 1024, backupCount=5)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add them to handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# Utility functions for logging
def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)

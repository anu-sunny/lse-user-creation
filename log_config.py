"""
log_config.py

Sets up logging to log errors and warnings to a file.

Author: Anu
Date: 2025-06-11
"""
# importing pythons built-in logging module for recording messages and error to a log file
import logging

# Configure logging to write to error_log.txt
logging.basicConfig(
    filename='error_log.txt',
    filemode='a',  # Append to the log file
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create logger instance
logger = logging.getLogger(__name__)
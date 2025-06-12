"""
validation.py

Contains validation functions for checking CSV row data.

Author: Anu
Date: 2025-06-11
"""
#import built in module for Regular Expression
import re
from log_config import logger

def is_valid_email(email):
    """
    Validates an email address using a regular expression.

    Parameters:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    if not email:
        logger.warning("Email is missing or empty.")
        return False

    # Basic email pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'   #r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email.strip()) is not None:
        logger.warning(f"Invalid email format: {email}")
        return False
        
    return True

def is_valid_row(row, required_fields):
    """
    Checks if all required fields are present and valid.

    Also validates email format.

    Parameters:
        row (dict): A CSV row.
        required_fields (list): List of required fields.

    Returns:
        bool: True if valid, False otherwise.
    """
    #for field in required_fields:
        #if not row.get(field) or not row[field].strip():
    if not all(row.get(field) and row.get(field).strip() for field in required_fields):
        logger.warning(f"Missing required field: {row}")
        return False

    # Additional check for email
    if not is_valid_email(row["email"]):
        
        return False

    return True

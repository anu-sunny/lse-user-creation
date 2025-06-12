"""
main.py

Reads user data from a CSV file and creates users by sending
POST requests to an API endpoint.

Author: Anu
Date: 2025-06-11
"""

import csv
#importing required functions
from log_config import logger				
from validation import is_valid_row 	
from api_requests import create_new_user

# Define required fields
REQUIRED_FIELDS = ["name", "email"]

def process_data(row):
    """
    Validates and processes a single row of user data.
    If the row is valid, sends a request to create the user.
    Logs and skips rows with missing required fields.
    
    Parameters:
    row (dict): A dictionary representing one row from the CSV.
    """
    if not is_valid_row(row, REQUIRED_FIELDS):
        logger.warning(f"Skipped row due to invalid fields: {row}")
        print(f"Skipped row: {row}")
        return
        
    if create_new_user(row):
        print(f"User created: {row['email']}")
    else:
        #Keep 'unknown' as a safe, defensive fallback.
        #logger.error(f"Error creating user: {row.get('email', 'unknown')}")
        print(f"Error creating user: {row.get('email', 'unknown')}")
      

def create_user(file_path):
    """
    Reads user data from a CSV file and processes each row.

    Parameters:
    file_path (str): Path to the CSV file containing user data.
    """
    try:
        with open(file_path, 'r',  encoding='utf-8') as f:	#added file encoding
            reader = csv.DictReader(f)
            # Process each row from the CSV file
            for row in reader:
                process_data(row)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        print(f"Error:File not found: {file_path}")
    except PermissionError:
        logger.error(f"Permission denied while opening file: {file_path}")
        print(f"Error:Permission denied: {file_path}")
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}", exc_info=True)
        print("Error reading CSV file")

# Entry point of the script
if __name__ == "__main__":
    create_user("users.csv")
 
 
"""
Suggestions: 
  
  -create seperate csv files for successfull/skipped rows.
  -email/teams notifications incase of failure.
  -notify user by email once account is successfully created.
  -a seperate log for success messages
  
"""

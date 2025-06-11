"""
api_requests.py

Handles API requests to create users.
"""
import requests
from log_config import logger

CREATE_USER_API = "https://example.com/api/create_user"

def create_new_user(user_data):
    """
    Sends a POST request to the user creation API.
    Logs an warning/error if the request fails.
    
    Parameters:
       user_data (dict): The user's data as a dictionary.

    Returns:
       bool: True if request was successful (status 201), False otherwise.
    
    """
    try:
        response = requests.post(CREATE_USER_API, json=user_data)
        if response.status_code != 201:
            logger.error(f"Failed to create user: {user_data.get('email', 'unknown')}, Status: {response.status_code}")
            return False
        return True
    except requests.RequestException as e:
        logger.error(f"Request error for user {user_data.get('email', 'unknown')}: {e}", exc_info=True)
        return False



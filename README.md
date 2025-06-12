# lse-user-creation
LSE - Support Engineer Coding Challenge

# User Creation via CSV & API

This Python project reads user data from a CSV file, validates each row (including email), and sends a POST request to an API to create users. 
It includes logging and error handling.

---

## Features

- ✅ Reads and processes CSV rows
- ✅ Validates required fields and email format
- ✅ Sends POST requests to a user creation API
- ✅ Logs all errors to a `.txt` file
- ✅ Skips invalid rows

---

## Project Structure

```bash
user_creation_project/
├── main.py               # Entry point
├── api_requests.py       # API request logic
├── validation.py         # Row and email validation
├── log_config.py         # Logging configuration
├── users.csv             # Sample CSV data
└── README.md             # Project description

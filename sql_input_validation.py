import re

def is_valid_username(username):
    # Username must be 3-20 characters long and contain only alphanumeric characters and underscores
    return re.match("^[a-zA-Z0-9_]{3,20}$", username) is not None

def is_valid_password(password):
    # Password must be 6-20 characters long and contain only alphanumeric characters and special characters
    return re.match("^[a-zA-Z0-9!@#$%^&*]{6,20}$", password) is not None

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

if not is_valid_username(username):
    print("Invalid username")
elif not is_valid_password(password):
    print("Invalid password")
else:
    # Proceed with processing (e.g., querying the database)
    pass

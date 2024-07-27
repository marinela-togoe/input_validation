import re
import html

def is_valid_input(input_string):
    # Example: Only allow alphanumeric characters, spaces, and a few punctuation marks
    return re.match("^[a-zA-Z0-9 .,!?-]{1,100}$", input_string) is not None

def sanitize_input(input_string):
    # Escape HTML special characters to prevent XSS
    return html.escape(input_string)

# Example usage
user_input = input("Enter your comment: ")

if is_valid_input(user_input):
    sanitized_input = sanitize_input(user_input)
    # Now, safe to store or display the sanitized input
    print("Safe output:", sanitized_input)
else:
    print("Invalid input")

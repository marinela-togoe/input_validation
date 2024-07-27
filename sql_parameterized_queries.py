import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Validate input
if is_valid_username(username) and is_valid_password(password):
    # Use parameterized queries to prevent SQL injection
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    if user:
        print("Login successful!")
    else:
        print("Invalid username or password.")
else:
    print("Invalid input")

# Close the connection
conn.close()

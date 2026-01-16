import sqlite3

conn = None

try:
    # Connect to (or create) the SQLite database
    conn = sqlite3.connect("../db/magazines.db")
    print("Database connected successfully.")

except sqlite3.Error as e:
    # Catch any SQLite-related errors
    print("An error occurred:", e)

finally:
    # Close the connection if it was opened
    if conn:
        conn.close()
        print("Database connection closed.")

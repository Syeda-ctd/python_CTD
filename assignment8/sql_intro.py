import sqlite3

conn = None

try:
    # Connect to the database
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")  # turn ON foreign key enforcement
    cursor = conn.cursor()

    # Create publishers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    # Create magazines table (one-to-many with publishers)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )
    """)

    # Create subscribers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    # Create subscriptions table (many-to-many)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
    )
    """)

    conn.commit()
    print("All tables created successfully.")

except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
    if conn:
        conn.close()
        print("Database connection closed.")

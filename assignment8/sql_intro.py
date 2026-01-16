import sqlite3

conn = None

try:
    # Connect to database
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")  # REQUIRED
    cursor = conn.cursor()

    # ---------- CREATE TABLES ----------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

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

    # ---------- FUNCTIONS ----------

    def add_publisher(name):
        try:
            cursor.execute(
                "INSERT INTO publishers (name) VALUES (?)",
                (name,)
            )
        except sqlite3.IntegrityError:
            print(f"Publisher '{name}' already exists.")

    def add_magazine(name, publisher_name):
        cursor.execute(
            "SELECT publisher_id FROM publishers WHERE name = ?",
            (publisher_name,)
        )
        result = cursor.fetchone()

        if not result:
            print(f"Publisher '{publisher_name}' not found.")
            return

        publisher_id = result[0]

        try:
            cursor.execute(
                "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
                (name, publisher_id)
            )
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists.")

    def add_subscriber(name, address):
        cursor.execute(
            "SELECT * FROM subscribers WHERE name = ? AND address = ?",
            (name, address)
        )
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
            return

        cursor.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?)",
            (name, address)
        )

    def add_subscription(subscriber_name, address, magazine_name, expiration):
        cursor.execute(
            "SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?",
            (subscriber_name, address)
        )
        s = cursor.fetchone()

        cursor.execute(
            "SELECT magazine_id FROM magazines WHERE name = ?",
            (magazine_name,)
        )
        m = cursor.fetchone()

        if not s or not m:
            print("Subscriber or magazine not found.")
            return

        subscriber_id = s[0]
        magazine_id = m[0]

        cursor.execute(
            """SELECT * FROM subscriptions
               WHERE subscriber_id = ? AND magazine_id = ?""",
            (subscriber_id, magazine_id)
        )
        if cursor.fetchone():
            print(f"{subscriber_name} already subscribed to {magazine_name}.")
            return

        cursor.execute(
            """INSERT INTO subscriptions
               (subscriber_id, magazine_id, expiration_date)
               VALUES (?, ?, ?)""",
            (subscriber_id, magazine_id, expiration)
        )

    # ---------- POPULATE TABLES ----------

    # Publishers
    add_publisher("Tech Media")
    add_publisher("Health Group")
    add_publisher("Science Press")

    # Magazines
    add_magazine("Tech Today", "Tech Media")
    add_magazine("Healthy Life", "Health Group")
    add_magazine("Science Weekly", "Science Press")

    # Subscribers
    add_subscriber("Alice Smith", "123 Main St")
    add_subscriber("Bob Jones", "456 Oak Ave")
    add_subscriber("Alice Smith", "789 Pine Rd")

    # Subscriptions
    add_subscription("Alice Smith", "123 Main St", "Tech Today", "2026-12-31")
    add_subscription("Bob Jones", "456 Oak Ave", "Healthy Life", "2026-06-30")
    add_subscription("Alice Smith", "789 Pine Rd", "Science Weekly", "2027-01-01")

    conn.commit()
    print("Data inserted successfully.")
    
    # ---------- TASK 4: SQL QUERIES ----------

    print("\n--- All Subscribers ---")
    cursor.execute("SELECT * FROM subscribers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print("\n--- All Magazines (Sorted by Name) ---")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print("\n--- Magazines Published by Tech Media ---")
    cursor.execute("""
        SELECT m.name, p.name
        FROM magazines m
        JOIN publishers p
        ON m.publisher_id = p.publisher_id
        WHERE p.name = ?
    """, ("Tech Media",))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
    if conn:
        conn.close()
        print("Database connection closed.")

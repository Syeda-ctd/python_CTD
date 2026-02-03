import sqlite3
import pandas as pd
import os

# Ensure the db folder exists
db_path = "../db/lesson.db"
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connect to the database
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # Enable foreign keys
    conn.execute("PRAGMA foreign_keys = 1")

    # --- Create tables ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL UNIQUE,
        price REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS line_items (
        line_item_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)

    # --- Insert sample data ---
    products = [
        ("Widget A", 10.5),
        ("Widget B", 7.25),
        ("Widget C", 12.0)
    ]

    line_items = [
        (1, 2),  # product_id=1, quantity=2
        (2, 5),
        (1, 3),
        (3, 1),
        (2, 4)
    ]

    # Insert products
    for name, price in products:
        try:
            cursor.execute("INSERT INTO products (product_name, price) VALUES (?, ?)", (name, price))
        except sqlite3.IntegrityError:
            pass  # ignore duplicates

    # Insert line_items
    for product_id, quantity in line_items:
        cursor.execute("INSERT INTO line_items (product_id, quantity) VALUES (?, ?)", (product_id, quantity))

    conn.commit()
    print("Sample database created successfully.")

    # --- Read data into Pandas ---
    sql_query = """
    SELECT
        li.line_item_id,
        li.quantity,
        li.product_id,
        p.product_name,
        p.price
    FROM line_items li
    JOIN products p ON li.product_id = p.product_id
    """
    df = pd.read_sql_query(sql_query, conn)

# --- Pandas operations ---
# Print first 5 rows
print("--- Raw Data ---")
print(df.head())

# Add total column
df['total'] = df['quantity'] * df['price']
print("\n--- With Total ---")
print(df.head())

# Group by product_id
summary_df = df.groupby('product_id').agg(
    line_item_count=('line_item_id', 'count'),
    total=('total', 'sum'),
    product_name=('product_name', 'first')
).reset_index()

# Sort by product_name
summary_df = summary_df.sort_values('product_name')

print("\n--- Summary ---")
print(summary_df.head())

# Write CSV
csv_path = "order_summary.csv"
summary_df.to_csv(csv_path, index=False)
print(f"\norder_summary.csv created at {os.path.abspath(csv_path)}")

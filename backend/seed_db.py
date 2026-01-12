# In backend/seed_db.py
import sqlite3
import os

def seed():
    db_path = 'ecommerce.db'
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT,
            stock INTEGER DEFAULT 0
        )
    ''')

    sample_products = [
        ('MacBook Pro M3', 2499.99, 'Laptop', 5),
        ('iPhone 15 Pro', 1199.00, 'Smartphone', 10),
        ('Logitech MX Master', 99.50, 'Accessori', 0), # Questo risulterà Out of Stock
        ('Monitor Dell 27"', 450.00, 'Monitor', 7),
        ('Cuffie Sony WH', 320.00, 'Audio', 3)
    ]

    cursor.executemany(
        "INSERT INTO products (name, price, category, stock) VALUES (?, ?, ?, ?)", 
        sample_products
    )

    conn.commit()
    conn.close()
    print("✅ Database rigenerato con colonna Stock!")

if __name__ == "__main__":
    seed()
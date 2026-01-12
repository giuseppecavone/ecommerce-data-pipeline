import sqlite3

class DBManager:
    def __init__(self, db_name="ecommerce.db"):
        self.conn = sqlite3.connect(db_name)
        self._init_db()

    def _init_db(self):
        query = '''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL,
                    category TEXT)'''
        self.conn.execute(query)
        self.conn.commit()

    def insert_product(self, name, price, category):
        query = "INSERT INTO products (name, price, category) VALUES (?, ?, ?)"
        with self.conn:
            self.conn.execute(query, (name, price, category))
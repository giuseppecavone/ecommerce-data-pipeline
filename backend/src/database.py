import sqlite3
from .decorators import log_execution

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../ecommerce.db")

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    @log_execution
    def create_tables(self):
        """Crea la struttura relazionale dell'e-commerce"""
        cursor = self.conn.cursor()
        
        # Tabella Prodotti
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT
            stock INTEGER DEFAULT 0
        )
        """)

        # Tabella Utenti (con Password Hashing)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """)

        # Tabella Ordini (Relazionata agli Utenti)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            total_price REAL NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """)
        
        self.conn.commit()

    @log_execution
    def insert_product(self, name, price, category):
        """Inserisce un singolo prodotto"""
        query = "INSERT INTO products (name, price, category) VALUES (?, ?, ?)"
        self.conn.execute(query, (name, price, category))
        self.conn.commit()

    def close(self):
        self.conn.close()
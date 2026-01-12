class OrderService:
    def __init__(self, db_manager):
        self.db = db_manager

    def checkout(self, user_id, cart_items):
        # cart_items è una lista di prodotti con i relativi prezzi
        total = sum(item['price'] for item in cart_items)
        
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO orders (user_id, total_price) VALUES (?, ?)",
            (user_id, total)
        )
        self.db.conn.commit()
        return {"order_id": cursor.lastrowid, "total": total, "status": "Success"}
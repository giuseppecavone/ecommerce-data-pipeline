class ProductService:
    def __init__(self, db_manager):
        self.db = db_manager

    def get_all_formatted(self):
        """Recupera i prodotti e applica logica di business (es. formattazione prezzo)"""
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1].upper(), # Esempio logica: nomi sempre in maiuscolo
                "price": round(row[2], 2),
                "category": row[3],
                "status": "In Stock" if row[2] > 0 else "Out of Stock"
            })
        return products

    def apply_discount(self, product_id, percentage):
        """Esempio di operazione di business complessa"""
        # Qui andrebbe la logica per aggiornare il prezzo nel DB
        pass
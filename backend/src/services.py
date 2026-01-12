from .exceptions import ValidationError

class ProductService:
    def __init__(self, db_manager):
        self.db = db_manager

    def get_all_formatted(self):
        try:
            cursor = self.db.conn.cursor()
            # Selezioniamo anche la colonna stock
            cursor.execute("SELECT id, name, price, category, stock FROM products")
            rows = cursor.fetchall()
            
            products = []
            for row in rows:
                products.append({
                    "id": row[0],
                    "name": row[1].upper(),
                    "price": round(row[2], 2),
                    "category": row[3],
                    "stock": row[4],
                    # Logica basata sullo stock reale
                    "status": "In Stock" if row[4] > 0 else "Out of Stock"
                })
            return products
        except Exception as e:
            print(f"Errore nel service: {e}")
            return []

    def create_product(self, data):
        """Valida e crea un nuovo prodotto"""
        name = data.get('name')
        price = data.get('price')
        
        # Logica di Validazione
        if not name or len(name) < 3:
            raise ValidationError("Il nome del prodotto deve avere almeno 3 caratteri")
        
        try:
            price_float = float(price)
            if price_float <= 0:
                raise ValidationError("Il prezzo deve essere un numero positivo")
        except (ValueError, TypeError):
            raise ValidationError("Il prezzo fornito non è un numero valido")

        # Se tutto è ok, salviamo nel DB tramite il manager
        self.db.insert_product(name, price_float, data.get('category', 'Generico'))
        return {"name": name, "price": price_float}
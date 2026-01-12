from flask import Flask, jsonify, request
from src.database import DBManager

app = Flask(__name__)
db = DBManager()

@app.route('/api/products', methods=['GET'])
def get_products():
    """Ritorna la lista di tutti i prodotti nel DB"""
    cursor = db.conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    # Trasformiamo i dati in una lista di dizionari per il JSON
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "category": row[3]
        })
    return jsonify(products), 200

@app.route('/api/products', methods=['POST'])
def add_product():
    """Aggiunge un nuovo prodotto via API"""
    data = request.get_json()
    
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Dati incompleti"}), 400
        
    db.insert_product(data['name'], data['price'], data.get('category', 'Generico'))
    return jsonify({"message": "Prodotto creato con successo"}), 201

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
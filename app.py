from flask import Flask, jsonify
from src.database import DBManager
from src.services import ProductService # Importiamo il nuovo strato

app = Flask(__name__)
db = DBManager()
product_service = ProductService(db) # Inizializziamo il servizio

@app.route('/api/products', methods=['GET'])
def get_products():
    # L'API delega tutto al Service Layer
    products = product_service.get_all_formatted()
    return jsonify(products), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
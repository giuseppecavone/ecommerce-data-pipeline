from flask import Blueprint, jsonify, request
from .database import DBManager
from .services import ProductService
from .user_service import UserService
from .order_service import OrderService
from .auth import token_required  # Il decoratore per proteggere le rotte

# Inizializzazione Blueprint
api_bp = Blueprint('api', __name__)

# Inizializzazione dei componenti Core
db = DBManager()
product_service = ProductService(db)
user_service = UserService(db)
order_service = OrderService(db)

# --- ROTTE PUBBLICHE (Prodotti) ---

@api_bp.route('/products', methods=['GET'])
def get_products():
    """Recupera il catalogo prodotti (Accesso libero)"""
    return jsonify(product_service.get_all_formatted()), 200


# --- ROTTE AUTENTICAZIONE (JWT) ---

@api_bp.route('/register', methods=['POST'])
def register():
    """Registrazione nuovo utente"""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"status": "error", "message": "Dati incompleti"}), 400
    
    result = user_service.register_user(
        data['username'], 
        data['password'], 
        data.get('email', '')
    )
    return jsonify(result), 201

@api_bp.route('/login', methods=['POST'])
def login():
    """Login utente e rilascio Token JWT"""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"status": "error", "message": "Credenziali mancanti"}), 400
    
    result = user_service.login_user(data['username'], data['password'])
    
    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 401


# --- ROTTE PROTETTE (Richiedono JWT nel Header) ---

@api_bp.route('/checkout', methods=['POST'])
@token_required
def checkout(current_user_id):
    """
    Processa l'ordine dell'utente loggato.
    Il 'current_user_id' viene estratto automaticamente dal JWT dal decoratore.
    """
    data = request.get_json()
    if not data or 'cart' not in data:
        return jsonify({"status": "error", "message": "Carrello vuoto"}), 400
    
    result = order_service.checkout(current_user_id, data['cart'])
    return jsonify({
        "status": "success",
        "message": "Ordine effettuato con successo",
        "order_details": result
    }), 200
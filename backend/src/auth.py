from flask import request, jsonify
import jwt
from functools import wraps
from .user_service import UserService

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"message": "Token mancante!"}), 401
        
        try:
            # Rimuoviamo la parola 'Bearer ' se presente
            if "Bearer " in token:
                token = token.split(" ")[1]
            data = jwt.decode(token, UserService.SECRET_KEY, algorithms=["HS256"])
            current_user_id = data['user_id']
        except Exception:
            return jsonify({"message": "Token non valido o scaduto!"}), 401

        return f(current_user_id, *args, **kwargs)
    return decorated
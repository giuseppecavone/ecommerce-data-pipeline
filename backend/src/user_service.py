import jwt
import datetime
# Queste sono le funzioni già presenti in Flask (Werkzeug)
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def __init__(self, db_manager):
        self.db = db_manager
        # Chiave segreta per il JWT
        self.SECRET_KEY = "infinity_tech_secret_key_2024"

    def register_user(self, username, password, email):
        """Registra un utente hashando la password con Werkzeug"""
        # Crea un hash sicuro con sale incluso (es: pbkdf2:sha256:600000$...)
        hashed_pw = generate_password_hash(password)
        
        try:
            cursor = self.db.conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (username, hashed_pw, email)
            )
            self.db.conn.commit()
            return {"status": "success", "message": "Utente registrato!"}
        except Exception as e:
            print(f"Errore DB: {e}")
            return {"status": "error", "message": "Username o Email già esistenti"}

    def login_user(self, username, password):
        """Verifica la password nativa e genera il JWT"""
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        # check_password_hash verifica l'hash memorizzato contro la password inserita
        if user and check_password_hash(user[1], password):
            payload = {
                "user_id": user[0],
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }
            
            # Generazione del token JWT per il frontend
            token = jwt.encode(payload, self.SECRET_KEY, algorithm="HS256")
            
            return {
                "status": "success", 
                "token": token, 
                "message": f"Bentornato {username}!"
            }
        
        return {"status": "error", "message": "Credenziali non valide"}
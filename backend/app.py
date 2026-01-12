from flask import Flask, jsonify
from src.api_routes import api_bp # Importiamo il modulo delle rotte
from src.exceptions import EcommerceError
from flask_cors import CORS
import os
from flask import send_from_directory

app = Flask(__name__)
CORS(app)

@app.route('/favicon.ico')
def favicon():
    # Invia il file dalla cartella static
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# REGISTRAZIONE DEL BLUEPRINT
# Tutte le rotte in api_routes.py avranno ora il prefisso /api
app.register_blueprint(api_bp, url_prefix='/api')

# --- GESTORE ERRORI GLOBALE (Resta qui perché è una config del server) ---
@app.errorhandler(EcommerceError)
def handle_ecommerce_error(error):
    return jsonify({"status": "error", "message": error.message}), error.status_code

@app.errorhandler(Exception)
def handle_generic_error(error):
    return jsonify({"status": "error", "message": "Errore interno del server"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
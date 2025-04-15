# app.py

from flask import Flask
from database import db, init_db
from routes import api_bp

app = Flask(__name__)

# Inicializar la base de datos
init_db(app)

# Registrar las rutas
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
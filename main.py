# app/main.py
from flask import Flask
from flask_cors import CORS
from app.routes.auth_routes import auth_bp
from app.routes.hospital_routes import hospital_bp
from app.routes.chatbot_routes import chatbot_bp
from app.routes.insurance_routes import insurance_bp
from app.routes.feedback_routes import feedback_bp
from app.services.db_service import seed_db
import sys

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(hospital_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(insurance_bp)
    app.register_blueprint(feedback_bp)

    return app

app = create_app()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "seed":
        seed_db()
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)

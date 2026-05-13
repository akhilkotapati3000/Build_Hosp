# app/__init__.py
from flask import Flask
from flask_cors import CORS
from .routes.auth_routes import auth_bp
from .routes.hospital_routes import hospital_bp
from .routes.insurance_routes import insurance_bp
from .routes.chatbot_routes import chatbot_bp
from .routes.feedback_routes import feedback_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(hospital_bp, url_prefix="/api/hospitals")
    app.register_blueprint(insurance_bp, url_prefix="/api/insurance")
    app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")
    app.register_blueprint(feedback_bp, url_prefix="/api/feedback")

    # Root test route
    @app.route("/")
    def home():
        return {"message": "BuildHosp Backend is running!"}

    return app

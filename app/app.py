import os
from flask import Flask, jsonify, redirect
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from app.db import db
from app.resources.item import blp as ItemBlueprint
from app.resources.store import blp as StoreBlueprint
from app.resources.tag import blp as TagBlueprint
from app.resources.user import blp as UserBlueprint
from app.blocklist import BLOCKLIST

# ✅ Global migrate instance
migrate = Migrate()

def create_app(db_url=None):
    load_dotenv()
    app = Flask(__name__)

    # ---------------------- CONFIG ---------------------- #
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = None
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "274340523376240357978050443855663722512"

    # ---------------------- INIT EXTENSIONS ---------------------- #
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)
    jwt = JWTManager(app)

    # ---------------------- JWT CALLBACKS ---------------------- #
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "description": "The token has been revoked.",
            "error": "token_revoked"
        }), 401

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return jsonify({
            "description": "The token is not fresh.",
            "error": "fresh_token_required"
        }), 401

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        return {"is_admin": identity == 2}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "message": "The token has expired.",
            "error": "token_expired"
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            "message": "Signature verification failed.",
            "error": "invalid_token"
        }), 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            "description": "Request does not contain an access token.",
            "error": "authorization_required"
        }), 401

    # ---------------------- BLUEPRINTS ---------------------- #
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    # ---------------------- ROOT REDIRECT ---------------------- #
    @app.route("/")
    def index():
        return redirect("/swagger-ui/")

    return app

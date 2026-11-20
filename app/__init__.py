from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    from . import models
    db.init_app(app)
    with app.app_context():
        db.create_all()
    @app.route("/")
    def index():
        return {"status": "ok"}
    @app.route("/main/<name>")
    def main(name):
        return '<h1>lol, %s!' %name
    return app
from flask import Flask
from .extensions import db
from . import models
from .task_routes import bp as tasks_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    app.register_blueprint(tasks_bp)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    @app.route("/")
    def index():
        return {"status": "ok"}
    return app
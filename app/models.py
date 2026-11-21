from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db

class Task(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(10), nullable=False)
    deadline = db.Column(db.Date)
    is_done = db.Column(db.Boolean, default=False)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "deadline": self.deadline.isoformat() if self.deadline else None,
            "is_done": self.is_done
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        is_correct = check_password_hash(self.password_hash, password)
        return is_correct
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }
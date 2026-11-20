from .extensions import db

class Task(db.Model):
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
    
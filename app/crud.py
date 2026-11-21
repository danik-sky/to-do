from .extensions import db
from .models import Task

def create_task(title, priority, deadline=None):
    task = Task(title=title, priority=priority, deadline=deadline)
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks():
    query = db.select(Task).order_by(Task.id)
    tasks = db.session.scalars(query).all()
    return tasks

def get_task(task_id):
    task = db.session.get(Task, task_id)
    return task

def mark_done(task):
    task.is_done = True
    db.session.commit()
    return task

def delete_task(task):
    db.session.delete(task)
    db.session.commit()

from .extensions import db
from .models import Task, User

def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_username(username):
    query = db.select(User).where(User.username == username)
    user = db.session.scalar(query)
    return user

def create_task(title, priority, user_id, deadline=None):
    task = Task(user_id=user_id, title=title, priority=priority, deadline=deadline)
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks(user_id):
    query = db.select(Task).order_by(Task.id).where(Task.user_id == user_id)
    tasks = db.session.scalars(query).all()
    return tasks

def get_task(task_id, user_id):
    query = db.select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = db.session.scalar(query)
    return task

def mark_done(task):
    task.is_done = True
    db.session.commit()
    return task

def delete_task(task):
    db.session.delete(task)
    db.session.commit()

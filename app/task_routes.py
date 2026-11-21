from flask import Blueprint, request, session
from datetime import datetime
from . import crud

bp = Blueprint("tasks", __name__)

@bp.before_request
def require_login():
    if "user_id" not in session:
        return {"error": "login or register first"}, 401

@bp.route("/tasks")
def list_tasks():
    user_id = session["user_id"]
    tasks = crud.get_all_tasks(user_id)
    return [t.to_dict() for t in tasks]

@bp.route("/tasks/<int:task_id>")
def get_one_task(task_id):
    user_id = session["user_id"]
    task = crud.get_task(task_id, user_id)
    if not task:
        return {"error": "Task not found"}, 404
    return task.to_dict()

@bp.route("/create", methods = ["POST"])
def create():
    user_id = session["user_id"]
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return {"error": "Bad request for create"}, 400
    title = data.get("title")
    if (not isinstance(title, str)) or (title.strip()==""):
        return {"error": "title not correct"}, 400
    title = title.strip()
    priority = data.get("priority")
    if priority not in ["low", "medium", "high"]:
        return {"error": "priority not correct"}, 400
    deadline = data.get("deadline")
    if deadline is not None:
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        except(ValueError, TypeError):
            return {"error": "deadline not correct"}, 400   
    task = crud.create_task(title, priority, user_id, deadline)
    return task.to_dict(), 201

@bp.route("/tasks/<int:task_id>/done", methods=["POST"])
def done(task_id):
    user_id = session["user_id"]
    task = crud.get_task(task_id, user_id)
    if not task:
        return {"error": "Task not found"}, 404
    task = crud.mark_done(task)
    return task.to_dict()

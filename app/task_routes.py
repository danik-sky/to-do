from flask import Blueprint, request
from datetime import datetime
from . import crud

bp = Blueprint("tasks", __name__)

@bp.route("/tasks")
def list_tasks():
    tasks = crud.get_all_tasks()
    return [t.to_dict() for t in tasks]

@bp.route("/tasks/<int:task_id>")
def get_one_task(task_id):
    task = crud.get_task(task_id)
    if not task:
        return {"error": "Task not found"}, 404
    return task.to_dict()

@bp.route("/create", methods = ["POST"])
def create():
    data = request.get_json(silent=True)
    if not data:
        return {"error": "data is None"}, 400
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
    task = crud.create_task(title=title, priority=priority, deadline=deadline)
    return task.to_dict(), 201

@bp.route("/tasks/<int:task_id>/done", methods=["POST"])
def done(task_id):
    task = crud.get_task(task_id)
    if not task:
        return {"error": "Task not found"}, 404
    task = crud.mark_done(task)
    return task.to_dict()

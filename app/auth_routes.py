from flask import Blueprint, request, session
from . import crud

bp = Blueprint("auth", __name__)

@bp.route("/register", methods=["POST"])
def registration():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return {"error": "Bad request for register"}, 400
    username = data.get("username")
    if (not isinstance(username, str)) or (username.strip()==""):
        return {"error": "username not correct"}, 400
    username = username.strip()
    password = data.get("password")
    if (not isinstance(password, str)) or (password.strip()==""):
        return {"error": "password not correct"}, 400
    if crud.get_user_by_username(username):
        return {"error": "username is already in use"}, 409
    user = crud.create_user(username, password)
    return user.to_dict(), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return {"error": "Bad request for login"}, 400
    username = data.get("username")
    if (not isinstance(username, str)) or (username.strip()==""):
        return {"error": "username not correct"}, 400
    username = username.strip()
    password = data.get("password")
    if (not isinstance(password, str)) or (password.strip()==""):
        return {"error": "password not correct"}, 400
    user = crud.get_user_by_username(username)
    if not user or not user.check_password(password):
        return {"error": "invalid username or password"}, 401
    session["user_id"] = user.id
    return {"message": "logged in", "user": user.to_dict()}

@bp.route("/logout", methods=["POST"])
def logout():
    session.pop("user_id", None)
    return {"message": "logged out"}
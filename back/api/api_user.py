import flask
from flask import Blueprint, current_app, request, jsonify
from sqlalchemy.exc import IntegrityError

api_user = Blueprint('api_user', __name__)


@api_user.record
def record(state):
    db = state.app.config.get("user.db")
    if db is None:
        raise Exception("This blueprint expects you to provide "
                        "database access through user.db")


@api_user.route('/api/login', methods=['POST'])
def login_user():
    user_db = current_app.config["user.db"]
    username = request.json["username"]
    user = user_db.find_user_by_name(username)
    if user is None:
        return "User doesn't exist", 404
    print(user)
    if user.password_hash == request.json["password"]:
        # tu dodaj ciateczko
        apikey_db = current_app.config["apikey.db"]
        apikey = apikey_db.find_apikey_by_name(username)
        if apikey is None:
            apikey = apikey_db.create_apikey(username)
        response = flask.make_response()
        response.set_cookie("apikey", value=apikey.apikey)
        return response  # "Login successful"
    return "Wrong password", 401


@api_user.route('/api/register', methods=['POST'])
def register_user():
    user_db = current_app.config["user.db"]
    apikey_db = current_app.config["apikey.db"]
    try:
        user = user_db.create_user(request.json["username"], request.json["email"], request.json["password"])
        apikey_db.create_apikey(user.username)
    except IntegrityError:
        return "User already exists", 400
    print(user)
    return jsonify(id=user.id, username=user.username, email=user.email)

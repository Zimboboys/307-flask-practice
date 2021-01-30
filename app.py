from flask import Flask, request, jsonify
from flask_cors import CORS

from model import User

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_wold():
    return 'hello world!'

@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')

        if search_username or search_job:
            search_condition = {}
            if search_username:
                search_condition["name"] = search_username
            if search_job:
                search_condition["job"] = search_job

            users = User().find_some(search_condition)
            return {"users_list": users}, 200

        users = User().find_all()
        return {"users_list": users}, 200

    elif request.method == 'POST':
        user = User(request.get_json())
        user.save()

        resp = jsonify(newCharacter=user, success=True)
        resp.status_code = 201
        return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        if id:
            user = User().find_id(id)
            if len(user) == 0:
                return jsonify(users_list=user, error="no users found"), 404
            return jsonify(users_list=user), 200
        return User().find_all(), 200

    elif request.method == 'DELETE':
        user = User({"_id":id})
        removed = user.remove()

        # pretty sure this'll get set if a delete error happens
        if removed.get('writeError'):
            return {}, 404
        return {}, 204

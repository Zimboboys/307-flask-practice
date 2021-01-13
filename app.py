from flask import Flask, request, jsonify
import json

app = Flask(__name__)

users = json.load(open('users.json', 'r'))

@app.route('/')
def hello_wold():
    return 'hello world!'

@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')

        if search_username or search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if ((not search_username or user['name'] == search_username)
                        and (not search_job or user['job'] == search_job)):
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      resp.status_code = 201
      return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
        return users
    elif request.method == 'DELETE':
        for user in users['users_list']:
            if user['id'] == id:
                users['users_list'].remove(user)
        return users

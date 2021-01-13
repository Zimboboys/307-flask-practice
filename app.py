from flask import Flask, request
import json

app = Flask(__name__)

users = json.load(open('users.json', 'r'))

@app.route('/')
def hello_wold():
    return 'hello world!'

@app.route('/users')
def get_users():
    search_username = request.args.get('name') # accessing the value of parameter 'name'
    if search_username:
        subdict = {'users_list' : []}
        for user in users['users_list']:
            if user['name'] == search_username:
                subdict['users_list'].append(user)
        return subdict
    return users

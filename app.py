from flask import Flask
import json

app = Flask(__name__)

users = json.load(open('users.json', 'r'))

@app.route('/')
def hello_wold():
    return 'hello world!'

@app.route('/users')
def get_users():
    return users

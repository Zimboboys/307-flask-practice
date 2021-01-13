# 307-flask-practice
setting up some simple endpoints with flask

data resides in `users.json`

## endpoints
`GET /users/` - get all users
- optional query parameters: `name` and `job` (filters by these)

`POST /users/` - adds new user

`GET /users/<id>` - get user by id

`DELETE /users/<id>` - delete a user by id

## running dev server
1. create a virtual env and install Flask
2. run `python3 -m flask run` to start the server
3. visit `http://localhost:5000`

import jwt

from flask import Flask, jsonify, request, Blueprint, make_response, current_app, abort

from app import mongo

auth_ = Blueprint('auth', __name__)

@auth_.route('/login', methods = ['POST'])
def index():
    body = request.get_json()

    email = body.get('email', None)
    password = body.get('password', None)

    
    if email == None or password == None:
        abort(400)

    user = mongo.db.user.find_one({"email": email})

    if user is None:
        return make_response(
            jsonify({
                "status": "ERROR",
                "message": "User not exists"
                }), 400
            )
    else:
        token = jwt.encode({
            "id": str(user.get('_id')),
            "name": user.get('name', None),
            "email": user.get('email')
            },
            current_app.config['SECRET_KEY'], algorithm = 'HS256')
        return make_response(
            jsonify({
                "status": "OK",
                "message": "Success Login",
                "token": token
            }), 200
        )
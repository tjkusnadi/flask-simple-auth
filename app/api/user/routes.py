from flask import Flask, jsonify, request, Blueprint, make_response, abort

from werkzeug.security import generate_password_hash



from app import mongo

user_ = Blueprint('user', __name__)

@user_.route('', methods = ['POST'])
def index():
    body = request.get_json()

    name = body.get('name', None)
    email = body.get('email', None)
    password = body.get('password', None)

    
    if email == None or password == None and name == None:
        abort(400)

    user = mongo.db.user.find_one({"email": email})

    if user is None:
        body['password'] = generate_password_hash(password, method='pbkdf2:sha256:200')
        register_user = mongo.db.user.insert_one(body)
        return make_response(
            jsonify({
                "status": "OK",
                "message": "Success register"
                }), 200
            )
    else:
        return make_response(
            jsonify({
                "status": "ERROR",
                "message": "User already exists"
                }), 400
            )

    
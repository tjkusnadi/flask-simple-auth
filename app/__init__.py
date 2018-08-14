from flask import Flask
from flask_pymongo import PyMongo


app  = Flask(__name__)
mongo = PyMongo()
def create_app():

    from app.api.user.routes import user_
    app.register_blueprint(user_,url_prefix='/api/user')

    from app.api.auth.routes import auth_
    app.register_blueprint(auth_, url_prefix='/api/auth')

    return app
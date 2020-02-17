# app
from flask import Flask
# api
from flask_restful import Api
# jwt
# from flask_jwt_extended import JWTManager

# from flask_restful_swagger import swagger

jwt = None


def create_app():
    """crear instancia de Flask app"""
    app = Flask(__name__)
    # app.config.from_pyfile('db/db_config.py')
    app.config.from_pyfile('config.py')
    # init jwt
    return app

def init_api(app):
    from .resource.AllUsers import AllUsers
    from .resource.Login import Login
    from .resource.ZonaPeligrosa import ZonaPeligrosa

    api = Api(app)
    api.add_resource(AllUsers, '/users')
    api.add_resource(Login, '/login')
    api.add_resource(ZonaPeligrosa, '/prediccion')


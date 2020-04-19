from flask import Flask
from flask_restful import Api


def create_app():
    """crear instancia de Flask app"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    return app

def init_api(app):
    from .resource.AllUsers import AllUsers
    from .resource.Login import Login
    from .resource.MultiPartEx import MultiPartEx

    api = Api(app)
    api.add_resource(AllUsers, '/users')
    api.add_resource(Login, '/login')
    api.add_resource(MultiPartEx, '/rafa')


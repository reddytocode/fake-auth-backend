# app
from flask import Flask
# api
from flask_restful import Api
# jwt
# from flask_jwt_extended import JWTManager

# from flask_restful_swagger import swagger

jwt = None
def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('db/db_config.py')
    app.config.from_pyfile('config.py')
    # init jwt
    return app

def init_api(app):
    from .resource.AllUsers import AllUsers

    api = Api(app)

    # api = swagger.docs(Api(app), apiVersion='0.1',
    #                    basePath='http://localhost:5000',
    #                    resourcePath='/',
    #                    produces=["application/json", "text/html"],
    #                    api_spec_url='/api/spec',
    #                    description='A Basic API')

    # api = swagger.docs(Api(app), apiVersion='0.1', api_spec_url='/doc')

    api.add_resource(AllUsers, '/users')


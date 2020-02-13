# # flask_web/app.py
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hey, we have Flask in a Docker container!'


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


from app import create_app, init_api
# try to change for db
# from app.db.db_extension import  db

from flask_jwt_extended import JWTManager
import unittest

app = create_app()
jwt = JWTManager(app)
init_api(app)
# db.init_app(app)
print("main running")
print("variable de entorno: ", app.config['SECRET_KEY'])



@app.errorhandler(404)
def not_found(error):
    return {"message": "Error 404"}

@app.errorhandler(500)
def not_found500(error):
    return {"message": "Error 500"}

if __name__ == '__main__':
    print("main")
    app.run(port=5000, host='0.0.0.0', debug = True)
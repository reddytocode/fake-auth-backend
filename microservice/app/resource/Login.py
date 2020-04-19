from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class Login(Resource):

    def post(self):
        data = parser.parse_args()
        return {"accessToken": "username-{}".format(data['username']), "refreshToken":"token goes here"}, 200
    def get(self):
        return {"message": "hola chichi"}
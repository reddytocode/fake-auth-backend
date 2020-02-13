from flask_restful import Resource, reqparse
# from ..model.UserModel import UserModel
parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class Login(Resource):
    def post(self):
        data = parser.parse_args()
        # return UserModel.return_all()
        return {"accessToken": "username-{}".format(data['id']), "refreshToken":"token goes here"}, 200
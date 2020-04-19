from flask_restful import Resource, reqparse
import werkzeug
import logging

# Este archivo es para recibir imagenes y archivos ademas de json
parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

class MultiPartEx(Resource):

    def post(self):
        data = parser.parse_args()
        logging.warning(data)
        audioFile = data['file']
        audioFile.save("your_file_name.jpg")
        # return UserModel.return_all()
        return {"message": "Hola rafa :v"}
        return {"accessToken": "username-{}".format(data['username']), "refreshToken":"token goes here"}, 200
    
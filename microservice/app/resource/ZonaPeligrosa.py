from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('index_zone', help='This field cannot be blank, chichi que te pasa mandame un index!', required=True)


def black_box(index_zone):
    """
    input: indice de la zona
    output: probabilidad de peligro
    """
    # call 2 regressiones

    return 3.6


class ZonaPeligrosa(Resource):

    def post(self):
        data = parser.parse_args()
        return {"probabilidad": black_box(data['index_zone'])}, 400

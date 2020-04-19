from flask_restful import Resource


class AllUsers(Resource):
    def get(self):
        return {"message":flask['secret_key']}, 200

    def delete(self):
        return {"message": "Deleted"}, 200
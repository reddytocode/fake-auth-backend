from flask_restful import Resource
# from ..model.UserModel import UserModel

class AllUsers(Resource):
    def get(self):
        # return UserModel.return_all()
        return {"message":flask['secret_key']}, 200

    def delete(self):
        # return UserModel.delete_all()
        return {"message": "Deleted"}, 200
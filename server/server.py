from flask import Flask, request
from flask_restful import Resource, Api
import pymongo

app = Flask(__name__)
api = Api(app)
myclient = pymongo.MongoClient("mongodb://root:example@mongo:27017/")
mydb = myclient['check_db']
#Т.к. юзается пока только одна коллекция
mycol = mydb["users"]



class AddUser(Resource):
    def get(self):
        name = request.args.get('username')
        if name == "":
            return {"status": "exception", "description": "no username field"}
        
        mycol.insert_one({"name": name, "info": "some info"})
        return {"status": "ok", "result": 1}


class RemoveUser(Resource):
    def get(self):
        name = request.args.get('username')
        if name == "":
            return {"status": "exception", "description": "no username field"}

        mycol.delete_one({"name": name})
        return {"status": "ok", "result": 1}


class CheckUser(Resource):
    def get(self):

        name = request.args.get('username')
        if name == "":
            return {"status": "exception", "description": "no username field"}
        if len(list(mycol.find({"name": name}))) != 0:
            return {"status": "ok", "result": 1}
        return {"status": "ok", "result": 0}


api.add_resource(AddUser, '/add_user')
api.add_resource(RemoveUser, '/remove_user')
api.add_resource(CheckUser, '/check_user')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

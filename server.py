import json
from flask import Flask, Response,request,render_template
import pymongo
from bson.objectid import  ObjectId
app= Flask(__name__)

try:
    if __name__ == '__main__':
        mongo= pymongo.MongoClient(
            host="localhost",
            port=27017,
            serverSelectionTimeoutMS=1000
        )
        db=mongo.company
        mongo.server_info()

except :
    print("Can not connect to db")


@app.route('/users/')
def get_some_users():
        data= list(db.users.find())
        return render_template('display.html',data=data)

@app.route('/users/home')
def home():
        return render_template('home.html')


@app.route("/add" ,methods=["POST"])
def create_user():
    if request.method == 'POST':
        user= {"name": request.form["name"],
               "lastname":request.form["lastname"]}
        dbResponse= db.users.insert_one(user)



        return Response(
            response= json.dumps(
                {"message":"user created"}),
            status=200,
            mimetype="application/json"

        )




if __name__ == "__main__":
    app.run(port=80,debug=True)


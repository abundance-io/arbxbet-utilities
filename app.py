from flask import Flask,request

from dbint import get_database
app = Flask(__name__)
from bson import ObjectId

dbname = get_database()
@app.route('/logout')
def logout():
    id = request.args.get("id")
    users = dbname["users"]
    users.update_one({"_id":ObjectId(id)},{"$set":{"loggedin":False}})
    return ''

    


if __name__=='__main__':
    app.run()
from flask import Flask
from flask import jsonify
from flask import request
from Logic import dbService, Authenticate
import json
app = Flask(__name__)

empDB=[
 {
 'id':'101',
 'name':'Dipankar S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Monali S',
 'title':'Sr Software Engineer'
 }
 ]

@app.route("/")
def hello():
    dbService.ReadData()
    return jsonify({'result': "Hello World!"})

@app.route('/employees',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/login', methods=['POST'])
def loginMember():
    requestData = (json.loads(request.data))
    
    try:    
        if(isStringNullorEmpty(requestData['username']) or isStringNullorEmpty(requestData['password'])):
            return jsonify({"message": "One or more parameters is missing from the request"}), 500
    except:
        return jsonify({"message": "One or more parameters is missing from the request"}), 500

    result = Authenticate.Auth(requestData['username'], requestData['password'])

    if  result["success"]:
        return jsonify(result)
    else:
        return jsonify({
            "success": False
        }), 401

def isStringNullorEmpty(str):
    if(not (str and str.strip())):
        return True
    else :
        return False

if __name__ == "__main__":
    app.run()
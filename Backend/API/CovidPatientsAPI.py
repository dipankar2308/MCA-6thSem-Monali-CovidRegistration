from flask import Flask
from flask import jsonify
from flask import request
from Logic import login, userDetails, userCredentials, userStatus, data
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'result': "Hello World!"})

@app.route('/user/auth/login', methods=['POST'])
def loginMember():
    requestData = (json.loads(request.data))
    
    try:    
        if(isStringNullorEmpty(requestData['username']) or isStringNullorEmpty(requestData['password'])):
            return jsonify({"message": "One or more parameters is missing from the request"}), 500
    except:
        return jsonify({"message": "One or more parameters is missing from the request"}), 500

    result = login.Auth(requestData['username'], requestData['password'])

    if  result["success"]:
        return jsonify(result)
    else:
        return jsonify({
            "success": False
        }), 401

@app.route('/user/auth/register', methods=['POST'])
def registerUser():
    requestData = (json.loads(request.data))
    
    try:    
        if(isStringNullorEmpty(requestData['username']) or isStringNullorEmpty(requestData['password'])):
            return jsonify({"message": "One or more parameters is missing from the request"}), 500
    except:
        return jsonify({"message": "One or more parameters is missing from the request"}), 500

    result = userCredentials.Register(requestData['username'], requestData['password'])

    return jsonify(result)

@app.route('/user/profile/<username>', methods=['POST'])
def updateProfile(username):
    requestData = (json.loads(request.data))

    try:
        if(isStringNullorEmpty(requestData['username']) or 
            isStringNullorEmpty(requestData['userId']) or 
            isStringNullorEmpty(requestData['name']) or 
            isStringNullorEmpty(requestData['area']) or 
            isStringNullorEmpty(requestData['city']) or 
            isStringNullorEmpty(requestData['phoneNumber']) or 
            isStringNullorEmpty(requestData['bloodGroup'])):
            return jsonify({"message": "all fields must be sent - username, userId, name, area, city, phoneNumber, bloodGroup"}), 400

        if(requestData['username'] != username):
            return jsonify({"message": "details of {0} expected, but request contains '{1}'".format(username, requestData['username'])})

        success = userDetails.Register(requestData)
    except NameError as err:
        print(err)
        return jsonify({"success": False}), 500

    return jsonify(success)

@app.route('/user/profile/<username>', methods=['GET'])
def getUserProfile(username):
    requestUsername = json.loads(request.data)

    if isStringNullorEmpty(str(requestUsername['userId'])):
        return jsonify({"message": "ID parameter is missing from the Request Body"})

    profileResponse = userDetails.GetProfile(username, requestUsername['userId'])

    if profileResponse['success']:
        return profileResponse
    
    return profileResponse, 400

@app.route('/user/profile/<username>/status', methods=['GET'])
def getMemberStatus(username):
    requestData = json.loads(request.data)

    if requestData['userId'] == None or isStringNullorEmpty(str(requestData['userId'])):
        return jsonify({
            "success": False,
            "message": "userId is missing in the request"
        }), 400

    result = userStatus.getuserStatusInformation(username, requestData['userId'])

    return jsonify(result)

@app.route('/user/profile/<username>/status', methods=['POST'])
def setMemberStatus(username):
    # {
    #     "id": 1,
    #     "memberStatus": "patient", // status = patient/donor
    # }
    requestData = json.loads(request.data)

    if ('userId' not in requestData or 
        requestData['userId'] == None or 
        isStringNullorEmpty(str(requestData['userId'])) or 
        'memberStatus' not in requestData or
        requestData['memberStatus'] == None or 
        isStringNullorEmpty(str(requestData['memberStatus']))):
        return jsonify({
            "success": False,
            "message": "One or more fields is missing in the request"
        }), 400
    
    result = userStatus.saveUserInformation(username, requestData['userId'], requestData['memberStatus'])

    return jsonify(result)

@app.route('/patients', methods= ['GET'])
def getAllPatients():
    requestData = json.loads(request.data)

    if ('userId' not in requestData or 
        isStringNullorEmpty(str(requestData['userId'])) or 
        'username' not in requestData or 
        isStringNullorEmpty(str(requestData['username']))):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            }), 400

    result = data.GetAllPatients(requestData['username'], requestData['userId'])
    return jsonify(result)

@app.route('/patients/<bloodGroup>', methods= ['GET'])
def getAllPatientsWithGroup(bloodGroup):
    requestData = json.loads(request.data)

    if ('userId' not in requestData or 
        isStringNullorEmpty(str(requestData['userId'])) or 
        'username' not in requestData or 
        isStringNullorEmpty(str(requestData['username']))):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            }), 400

    result = data.GetAllPatients(requestData['username'], requestData['userId'], bloodGroup)
    return jsonify(result)

@app.route('/data/bloodGroups', methods=['GET'])
def getAllBloodGroups():
    requestData = json.loads(request.data)

    if ('userId' not in requestData or 
        isStringNullorEmpty(str(requestData['userId'])) or 
        'username' not in requestData or 
        isStringNullorEmpty(str(requestData['username']))):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            }), 400
    
    return jsonify(data.getAllBloodGroups(requestData['username'], requestData['userId']))

@app.route('/donors', methods= ['GET'])
def getAllDonors():
    requestData = json.loads(request.data)

    if ('userId' not in requestData or 
        isStringNullorEmpty(str(requestData['userId'])) or 
        'username' not in requestData or 
        isStringNullorEmpty(str(requestData['username']))):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            })

    result = donors.GetAllDonors(requestData['username'], requestData['userId'])
    return jsonify(result)

@app.route('/donors/<bloodGroup>', methods= ['GET'])
def getAllDonorsWithGroup(bloodGroup):
    requestData = json.loads(request.data)

    if ('userId' not in requestData or 
        isStringNullorEmpty(str(requestData['userId'])) or 
        'username' not in requestData or 
        isStringNullorEmpty(str(requestData['username']))):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            })

    result = donors.GetAllDonors(requestData['username'], requestData['userId'], bloodGroup)
    return jsonify(result)

def isStringNullorEmpty(str):
    if(not (str and str.strip())):
        return True
    else :
        return False

if __name__ == "__main__":
    app.run()
from flask import Flask
from flask import jsonify
from flask import request
from Logic import login, userDetails, userStatus, data
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

    result = login.Register(requestData['username'], requestData['password'])

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
    requestUsername = request.args.get('userId')

    if isStringNullorEmpty(requestUsername):
        return jsonify({"message": "ID parameter is missing from the Request Body"})

    profileResponse = userDetails.GetProfile(username, requestUsername)

    if profileResponse['success']:
        return profileResponse
    
    return profileResponse, 400

@app.route('/user/profile/<username>/status', methods=['GET'])
def getMemberStatus(username):
    requestData = request.args.get('userId')

    if isStringNullorEmpty(requestData):
        return jsonify({
            "success": False,
            "message": "userId is missing in the request"
        }), 400

    result = userStatus.getuserStatusInformation(username, requestData)

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
    userId = request.args.get('userId')
    username = request.args.get('username')

    if (isStringNullorEmpty(userId) or 
        isStringNullorEmpty(username)):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            }), 400

    result = data.GetAllPatients(username, userId)
    return jsonify(result)

@app.route('/patients/<bloodGroup>', methods= ['GET'])
def getAllPatientsWithGroup(bloodGroup):
    userId = request.args.get('userId')
    username = request.args.get('username')

    if (isStringNullorEmpty(userId) or 
        isStringNullorEmpty(username)):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            }), 400

    result = data.GetAllPatientsWithGroup(username, userId, bloodGroup)
    return jsonify(result)

@app.route('/patients/profile/<id>', methods=['GET'])
def getPatientProfileById(id):
    username = request.args.get('username')
    userId = request.args.get('userId')

    if (isStringNullorEmpty(str(id)) or 
        isStringNullorEmpty(username) or 
        isStringNullorEmpty(userId)):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            }), 400

    result = data.GetAllPatientsWithId(username, userId, id)
    return jsonify(result)

@app.route('/data/bloodGroups', methods=['GET'])
def getAllBloodGroups():
    username = request.args.get('username')
    userId = request.args.get('userId')

    if (isStringNullorEmpty(str(userId)) or 
        isStringNullorEmpty(username)):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            }), 400
    
    return jsonify(data.getAllBloodGroups(username, userId))

@app.route('/donors', methods= ['GET'])
def getAllDonors():
    username = request.args.get('username')
    userId = request.args.get('userId')

    if (isStringNullorEmpty(userId) or 
        isStringNullorEmpty(username)):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            })

    result = data.GetAllDonors(username, userId)
    return jsonify(result)

@app.route('/donors/<bloodGroup>', methods= ['GET'])
def getAllDonorsWithGroup(bloodGroup):
    username = request.args.get('username')
    userId = request.args.get('userId')

    if (isStringNullorEmpty(userId) or 
        isStringNullorEmpty(username)):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            })

    result = data.GetAllDonorsWithGroup(username, userId, bloodGroup)
    return jsonify(result)

@app.route('/donors/profile/<id>', methods=['GET'])
def getDonorProfileById(id):
    username = request.args.get('username')
    userId = request.args.get('userId')

    if (isStringNullorEmpty(userId) or 
        isStringNullorEmpty(username)):
            return jsonify({
                "success": False,
                "message": 'One or more request parameters missing in request'
            })

    result = data.GetAllDonorsWithId(username, userId, id)
    return jsonify(result)

def isStringNullorEmpty(str):
    if(not (str and str.strip())):
        return True
    else :
        return False

if __name__ == "__main__":
    app.run()
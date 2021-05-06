from Logic.DB import dbService
from Logic import userDetails

def saveUserInformation(username, id, status):
    verifyUser = userDetails.GetProfile(username, id)

    if verifyUser['success']:
        userStatus = dbService.GetUserStatus(id)
        if userStatus!= None and userStatus['status'] == 'patient' and status == 'patient':
            return {
                "success": False,
                "message": "User is already registered as a Patient"
            }
        elif userStatus!= None and userStatus['status'] == 'donor' and status == 'donor':
            return {
                "success": False,
                "message": "User is already registered as a Donor"
            }
        else:
            if status == 'patient':
                # Add the member in patients list
                addPatientResult = dbService.SetUserStatusPatient(id)

                if addPatientResult:
                    # Delete the member from donor list
                    deleteDonorResult = dbService.DeleteDonor(id)
                    if deleteDonorResult:
                        return {
                            'success': True,
                            'message': 'User updated as a patient'
                        }
                    return {
                            'success': False,
                            'message': 'User not updated as a patient from donor'
                        } 
                else:
                    return {
                            'success': False,
                            'message': 'User not updated as a patient'
                        }
            elif status == 'donor':
                # Add member in donor list
                addDonorResult = dbService.SetUserStatusDonor(id)

                if addDonorResult:
                    # Delete member from patient list
                    deletePatientResult = dbService.DeletePatient(id)
                    if deletePatientResult:
                        return {
                            'success': True,
                            'message': 'User updated as a donor'
                        }
                    return {
                            'success': False,
                            'message': 'User not updated as a donor from patient'
                        } 

                else:
                    return {
                        'success': False,
                        'message': 'User not updated as a donor'
                    }
            else:
                return {
                    'success': False,
                    'message': 'Invalid status supplied'
                }
    else:
        return {
            "success": False,
            "message": verifyUser['message']
        }

def getuserStatusInformation(username, id):
    userProfile = userDetails.GetProfile(username, id)

    if userProfile['success']:
        userStatusDetails = dbService.GetUserStatus(id)
        if userStatusDetails == None:
            return {
                'success': False,
                'userProfile': "User status not found in DB"
            }    
        return {
            'success': True,
            'userProfile': userStatusDetails
        }
    else:
        return {
            'success': False,
            'message': userProfile['message']
        }

from Logic.DB import dbService
from Logic.Utils import bloodGroupValidator

def GetAllPatients(username, id):
    isUserExists = dbService.FindUserWithID(username, id)
    if isUserExists == 1:
        results = dbService.GetAllPatients()

        if results != None and len(results) > 0:
            return {
                'success': True,
                'patients': results
            }
        
        return {
            'success': True,
            'patients': []
        }
    elif isUserExists == -1:
        return {
            "success": False,
            "message": "No records in credentials found."
        }
    return {
            "success": False,
            "message": "Username and userId fields are mismatched."
        }

def GetAllPatientsWithGroup(username, id, bloodGroup):

    if bloodGroupValidator.isValidBloodGroup(bloodGroup):
        isUserExists = dbService.FindUserWithID(username, id)
        if isUserExists == 1:
            results = dbService.GetAllPatientsWithGroup(bloodGroup)

            if results != None and len(results) > 0:
                return {
                    'success': True,
                    'patients': results
                }
            
            return {
                'success': True,
                'patients': []
            }
        elif isUserExists == -1:
            return {
                "success": False,
                "message": "No records in credentials found."
            }
        return {
                "success": False,
                "message": "Username and userId fields are mismatched."
            }
    else:
        return {
            'success': False,
            'message': 'Invalid Blood group'
        }

def GetAllPatientsWithId(username, id, patientId):
    isUserExists = dbService.FindUserWithID(username, id)
    if isUserExists == 1:
        results = dbService.GetAllPatientsWithId(patientId)

        if results != None and len(results) > 0:
            return {
                'success': True,
                'patients': results
            }
        
        return {
                'success': True,
                'patients': []
            }
    elif isUserExists == -1:
        return {
            "success": False,
            "message": "No records in credentials found."
        }
    return {
            "success": False,
            "message": "Username and userId fields are mismatched."
        }

def GetAllDonors(username, id):
    isUserExists = dbService.FindUserWithID(username, id)
    if isUserExists == 1:
        results = dbService.GetAllDonors()

        if results != None and len(results) > 0:
            return {
                'success': True,
                'donors': results
            }
        
        return {
            'success': True,
            'donors': []
        }
    elif isUserExists == -1:
        return {
            "success": False,
            "message": "No records in credentials found."
        }
    return {
            "success": False,
            "message": "Username and userId fields are mismatched."
        }

def GetAllDonorsWithGroup(username, id, bloodGroup):
    if bloodGroupValidator.isValidBloodGroup(bloodGroup):
        isUserExists = dbService.FindUserWithID(username, id)
        if isUserExists == 1:
            results = dbService.GetAllDonorsWithGroup(bloodGroup)

            if results != None and len(results) > 0:
                return {
                    'success': True,
                    'donors': results
                }
            
            return {
                'success': True,
                'donors': []
            }
        elif isUserExists == -1:
            return {
                "success": False,
                "message": "No records in credentials found."
            }
        return {
                "success": False,
                "message": "Username and userId fields are mismatched."
            }
    else:
        return {
            'success': False,
            'message': 'Invalid Blood group'
        }

def GetAllDonorsWithId(username, id, donorId):
    isUserExists = dbService.FindUserWithID(username, id)
    if isUserExists == 1:
        results = dbService.GetAllDonorsWithId(donorId)

        if results != None and len(results) > 0:
            return {
                'success': True,
                'donors': results
            }
        
        return {
                'success': True,
                'donors': []
            }
    elif isUserExists == -1:
        return {
            "success": False,
            "message": "No records in credentials found."
        }
    return {
            "success": False,
            "message": "Username and userId fields are mismatched."
        }

def getAllBloodGroups(username, id):
    isUserExists = dbService.FindUserWithID(username, id)
    if isUserExists == 1:
        results = bloodGroupValidator.GetAllBloodGroups()
        return {
                'success': True,
                'bloodGroups': results['bloodGroups']
            }
    elif isUserExists == -1:
        return {
            "success": False,
            "message": "No records in credentials found."
        }
    return {
            "success": False,
            "message": "Username and userId fields are mismatched."
        }
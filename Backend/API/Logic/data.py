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
            'success': False
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

def GetAllPatients(username, id, bloodGroup):

    if bloodGroupValidator.isValidBloodGroup(bloodGroup):
        isUserExists = dbService.FindUserWithID(username, id)
        if isUserExists == 1:
            results = dbService.GetAllPatients(bloodGroup)

            if results != None and len(results) > 0:
                return {
                    'success': True,
                    'patients': results
                }
            
            return {
                'success': False,
                'patients': None
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
            'success': False
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

def GetAllDonors(username, id, bloodGroup):
    if bloodGroupValidator.isValidBloodGroup(bloodGroup):
        isUserExists = dbService.FindUserWithID(username, id)
        if isUserExists == 1:
            results = dbService.GetAllDonors(bloodGroup)

            if results != None and len(results) > 0:
                return {
                    'success': True,
                    'donors': results
                }
            
            return {
                'success': False,
                'donors': False
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
from Logic.DB import dbService

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
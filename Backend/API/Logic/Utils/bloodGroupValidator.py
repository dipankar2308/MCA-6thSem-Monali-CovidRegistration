validGroups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

def GetAllBloodGroups():
    return {
        'bloodGroups': validGroups
    }

def isValidBloodGroup(bloodGRoup):
    for group in validGroups:
        if group == bloodGRoup.upper():
            return True
    
    return False

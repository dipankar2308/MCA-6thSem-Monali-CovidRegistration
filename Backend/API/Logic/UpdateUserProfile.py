from Logic import dbService
import json

def Register(requestData):
    result = dbService.FindUserWithID(requestData['username'], requestData['userId'])
    # If the user credentials are found, check if user registration exists
    if result == 1:
        # User credentials are found
        print("User credentials found from before")
        existingRegistration = dbService.FindUserRegistration(requestData['userId'])

        success = False

        if existingRegistration == None:

            # User Registration is found. Update the existing one.
            success = dbService.AddUserProfile(
                requestData['userId'], 
                requestData['username'], 
                requestData['name'], 
                requestData['area'], 
                requestData['city'], 
                requestData['phoneNumber'], 
                requestData['bloodGroup'])
        else:

            # User Registration is not found. Create new one.
            success = dbService.UpdateProfile(
                requestData['userId'], 
                requestData['username'], 
                requestData['name'], 
                requestData['area'], 
                requestData['city'], 
                requestData['phoneNumber'], 
                requestData['bloodGroup'])

        if success:
            return {
            "success": success,
            "message": "User details updated successfully in system."
        }
        return {
            "success": False,
            "message": "User details could not be updated. Please try again later"
        }

    elif result == -1:
        # User credentials are not found
        print("User credentials not found")
        return {
            "success": False,
            "message": "User must register credentials first."
        }
    else:
        # Entry found in DB but data elements mismatched in validation
        return {
            "success": False,
            "message": "Mismatch in User-id and Username. Please verify the data and try again."
        }

    
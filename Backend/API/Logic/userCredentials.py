from Logic.DB import dbService
from Logic.Utils import Encode

def Register(username, password):
    encodedString = Encode.encodeString(password)

    result = dbService.RegisterUserInDB(username, encodedString)
    if result >= 0:
        return {
            "memberId": result,
            "success": True
        }
    elif result == -999:
        return {
            "message": "Username already exists in the system. Please select a different username.",
            "success": False
        }
    else:
        return {
            "message": "Unable to register new users at this time. Please try again later.",
            "success": False
        }
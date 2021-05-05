from Logic import dbService, Encode
import json

def Auth(username, password):
    encodedString = Encode.encodeString(password)
    result = dbService.FindUser(username, encodedString)
    
    if result >= 0:
        return {
            "memberId": result,
            "success": True
        }
    else:
        return {
            "success": False
        }
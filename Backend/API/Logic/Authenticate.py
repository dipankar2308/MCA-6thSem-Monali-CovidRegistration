from Logic import dbService
import json

def Auth(username, password):
    result = dbService.FindUser(username, password)
    if result >= 0:
        return {
            "memberId": result,
            "success": True
        }
    else:
        return {
            "success": False
        }
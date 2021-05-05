import mysql.connector
from Logic import Encode, Decode

def openConnection():
      mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="admin",
            password="password1"
      )
      return mydb

finduserQueryFormat = "SELECT * FROM covid19donor.credentials where userId like '{0}' and password like '{1}'"
findUserWithIdQuery = "SELECT * FROM covid19donor.credentials where memberId like '{0}' or userId like '{1}'"
findUserWithIdAndUsernameQuery = "SELECT * FROM covid19donor.credentials where userId like %s and memberId like %s"
findLastMemberIdQuery = 'select max(memberId) from covid19donor.credentials'
insertUsersQuery = "INSERT INTO `covid19donor`.`credentials` (`userId`, `password`, `memberId`) VALUES (%s, %s, %s)"
insertUserProfileQuery = "INSERT INTO `covid19donor`.`member` (`memberId`,`name`,`area`,`phoneNumber`,`bloodGroup`,`city`,`isActive`) VALUES (%s,%s,%s,%s,%s,%s,1)"
updateUserProfileQuery = "UPDATE `covid19donor`.`member` SET `memberId` = %s, `name` = %s, `area` = %s, `phoneNumber` = %s,`bloodGroup` = %s,`city` = %s, `isActive` = 1 WHERE memberId = %s;"
findUserRegistrationQuery = "SELECT * FROM covid19donor.member where memberId like '{0}'"

def FindUser(username, password):
      mydb = openConnection()
      mycursor = mydb.cursor()

      userQueryFormat = finduserQueryFormat
      
      mycursor.execute(userQueryFormat.format(username,password))
      myresult = mycursor.fetchall()

      for user in myresult:
            print(user)
            return user[2]
      
      mydb.close()
      return -1

def FindUserWithID(username, id):
      mydb = openConnection()
      myCursor = mydb.cursor()

      print(findUserWithIdQuery.format(id, username))
      myCursor.execute(findUserWithIdQuery.format(id, username))
      results = myCursor.fetchall()
      userResult = None

      for userId, password, memberId in results:
            userResult = {'username': userId, 'memberId': memberId}
            
            print("memberID = {0}, userId = {1}".format(str(userResult['memberId']), str(userId)))
            
            if userResult['username'] == username and str(userResult['memberId']) == str(id):
                  print("Matching records in credentials found")
                  return 1
      
      print(userResult)

      if userResult == None:
            print("No records in credentials found")
            return -1
      else:
            print("Mismatching records in credentials found")
            return 0

def RegisterUserInDB(username, password):
      mydb = openConnection()
      mycursor = mydb.cursor()

      findRecentMemberIdFormat = findLastMemberIdQuery
      mycursor.execute(findRecentMemberIdFormat)
      myresult = mycursor.fetchall()

      latestUserId = 0

      for entry in myresult:
            latestUserId = entry[0]
      if latestUserId:
            latestUserId += 1
      else:
            latestUserId = 1

      values = (username, password, latestUserId)

      try:
            mycursor.execute(insertUsersQuery, values)
            mydb.commit()
      except mysql.connector.IntegrityError:
            # print("Error received: {0}".format(err))
            return -999
      except:
            return -1
      mydb.close()
      return latestUserId

def AddUserProfile(userId, username, name, area, city, phoneNumber, bloodGroup):
      mydb = openConnection()
      mycursor = mydb.cursor()
      values = (userId, name, area, phoneNumber, bloodGroup, city)
      try:
            mycursor.execute(insertUserProfileQuery, values)
            mydb.commit()
      except mysql.connector.IntegrityError as err:
            print("Error received: {0}".format(err))
            return False
      except:
            print("Error received.")
            return False
      return True

def UpdateProfile(id, username, name, area, city, phoneNumber, bloodGroup):
      mydb = openConnection()
      mycursor = mydb.cursor()

      values = (id, name, area, phoneNumber, bloodGroup, city, id)
      try:
            mycursor.execute(updateUserProfileQuery, values)
            mydb.commit()
      except mysql.connector.IntegrityError as err:
            print("Error received: {0}".format(err))
            return False
      except:
            print("Error received.")
            return False
      
      mydb.close()
      return True

def FindUserRegistration(id):
      mydb = openConnection()
      mycursor = mydb.cursor()
      print("userId: {0}".format(id))

      try:
            mycursor.execute(findUserRegistrationQuery.format(id))
            results = mycursor.fetchall()

            row = None

            for memberId, name, area, phoneNumber, bloodGroup, city, isActive in results:
                  row = {
                        'userId': memberId, 
                        'name': name,
                        'area': area,
                        'phoneNumber': phoneNumber,
                        'bloodGroup': bloodGroup,
                        'city': city,
                  }
            print("Row: {0}".format(row))
            return row
      except mysql.connector.Error as err:
            print("Error in finding User Registration: {0}".format(err))
            return None
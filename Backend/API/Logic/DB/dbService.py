import mysql.connector
from mysql.connector.errors import Error
import datetime

def isProd():
      return False

def openConnection():
      if isProd():
            mydb = mysql.connector.connect(
                  host="remotemysql.com",
                  user="bKQOoH3XIM",
                  password="rIFOpdNfuG",
                  database='bKQOoH3XIM'
            )
            return mydb     
      
      mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="admin",
            password="password1",
            auth_plugin='mysql_native_password',
            database='covid19donor'
      )
      return mydb

finduserQueryFormat = "SELECT * FROM credentials where userId like '{0}' and password like '{1}'"
findUserWithIdQuery = "SELECT * FROM credentials where memberId like '{0}' or userId like '{1}'"
findUserWithIdAndUsernameQuery = "SELECT * FROM credentials where userId like %s and memberId like %s"
findLastMemberIdQuery = 'select max(memberId) from credentials'
insertUsersQuery = "INSERT INTO `credentials` (`userId`, `password`, `memberId`) VALUES (%s, %s, %s)"
insertUserProfileQuery = "INSERT INTO `member` (`memberId`,`name`,`area`,`phoneNumber`,`bloodGroup`,`city`,`isActive`) VALUES (%s,%s,%s,%s,%s,%s,1)"
updateUserProfileQuery = "UPDATE `member` SET `memberId` = %s, `name` = %s, `area` = %s, `phoneNumber` = %s,`bloodGroup` = %s,`city` = %s, `isActive` = 1 WHERE memberId = %s;"
findUserRegistrationQuery = "SELECT * FROM member where memberId like '{0}'"
findUserStatusFromPatient = "SELECT * FROM patients where memberId like '{0}' ORDER BY idpatients DESC LIMIT 1"
finduserStatusFromDonor = "SELECT * FROM donors where memberId like '{0}' ORDER BY iddonors DESC LIMIT 1"
findLastDonorId = "SELECT max(iddonors) as id from donors"
findLastPatientId = "SELECT max(idpatients) as id from patients"
insertDonorsQuery = "INSERT INTO `donors` (`iddonors`, `memberId`, `dateOfRequest`) VALUES ('{0}','{1}','{2}');"
insertPatientsQuery = "INSERT INTO `patients` (`idpatients`, `memberId`, `dateOfRequest`) VALUES ('{0}','{1}','{2}');"
deletePatientsQuery = "DELETE FROM `patients` WHERE memberId = '{0}'"
deleteDonorsQuery = "DELETE FROM `donors` WHERE memberId = '{0}'"
getAllPatientsQuery = "SELECT p.memberid as userId, m.name as name, m.area as area, m.bloodgroup as bloodgroup, m.city as city FROM patients p left join member m on p.memberId = m.memberId"
getPatientsByIdQuery = "SELECT p.memberid as userId, m.name as name, m.area as area, m.bloodgroup as bloodgroup, m.city as city from patients p left join member m on p.memberId = m.memberId where p.memberId like '{0}'"
getAllPatientsBloodQuery = "SELECT p.memberid as userId, m.name as name, m.area as area, m.bloodgroup as bloodgroup, m.city as city from patients p left join member m on p.memberId = m.memberId where m.bloodGroup like '{0}'"
getAllDonorQuery = "SELECT p.memberid as userId, m.name as name, m.area as area, m.bloodgroup as bloodgroup, m.city as city FROM donors p left join member m on p.memberId = m.memberId"
getDonorsByIdQuery = "SELECT p.memberid as userId, m.name as name, m.area as area, m.bloodgroup as bloodgroup, m.city as city from donors p left join member m on p.memberId = m.memberId where p.memberId like '{0}'"
getAllDonorBloodQuery = "SELECT p.memberid as userId, m.name as name, m.area as area, m.bloodgroup as bloodgroup, m.city as city FROM donors p left join member m on p.memberId = m.memberId where m.bloodGroup like '{0}'"

def FindUser(username, password):
      mydb = openConnection()
      mycursor = mydb.cursor()

      userQueryFormat = finduserQueryFormat
      
      mycursor.execute(userQueryFormat.format(username,password))
      myresult = mycursor.fetchall()
      mydb.close()

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
      mydb.close()
      if userResult == None:
            print("No records in credentials found")
            mydb.close()
            return -1
      else:
            print("Mismatching records in credentials found")
            mydb.close()
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
            mydb.close()
      except mysql.connector.IntegrityError as err:
            mydb.rollback()
            mydb.close()
            # print("Error received: {0}".format(err))
            return -999
      except:
            mydb.rollback()
            mydb.close()
            return -1

      return latestUserId

def AddUserProfile(userId, username, name, area, city, phoneNumber, bloodGroup):
      mydb = openConnection()
      mycursor = mydb.cursor()
      values = (userId, name, area, phoneNumber, bloodGroup, city)
      try:
            mycursor.execute(insertUserProfileQuery, values)
            mydb.commit()
            mydb.close()
      except mysql.connector.IntegrityError as err:
            print("Error received: {0}".format(err))
            mydb.close()
            return False
      except:
            print("Error received.")
            mydb.close()
            return False
      return True

def UpdateProfile(id, username, name, area, city, phoneNumber, bloodGroup):
      mydb = openConnection()
      mycursor = mydb.cursor()

      values = (id, name, area, phoneNumber, bloodGroup, city, id)
      try:
            mycursor.execute(updateUserProfileQuery, values)
            mydb.commit()
            mydb.close()
      except mysql.connector.IntegrityError as err:
            print("Error received: {0}".format(err))
            mydb.close()
            return False
      except:
            print("Error received.")
            mydb.close()
            return False

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
            mydb.close()
            return row
      except mysql.connector.Error as err:
            print("Error in finding User Registration: {0}".format(err))
            mydb.close()
            return None

# Get the current user status whether patient or donor
def GetUserStatus(userId):
      mydb = openConnection()
      myCursor = mydb.cursor()

      try:
            myCursor.execute(findUserStatusFromPatient.format(userId))
            results = myCursor.fetchall()
            row = None

            for iddonors, memberId, dateOfRequest in results:
                  row = {
                        'id': memberId,
                        'dateOfRequest': dateOfRequest,
                        'status': 'patient'
                  }
                  print (row)
            
            if row == None:
                  myCursor.execute(finduserStatusFromDonor.format(userId))
                  results = myCursor.fetchall()
                  for iddonors, memberId, dateOfRequest in results:
                      row = {
                        'id': memberId,
                        'dateOfRequest': dateOfRequest,
                        'status': 'donor'
                  }
                  print (row)

            mydb.close()
            return row
      except mysql.connector.Error as err:
            print("Error in finding User Registration: {0}".format(err))
            mydb.close()
            return None

#Get All Patients
def GetAllPatients():
      mydb = openConnection()
      mycursor = mydb.cursor()
      patients = []
      
      try:
            mycursor.execute(getAllPatientsQuery)
            myresult = mycursor.fetchall()
            mydb.close()

            for userId, name, area, bloodgroup, city in myresult:
                  print({
                        'userId': userId,
                        'name': name,
                        'area': area,
                        'bloodGroup': bloodgroup,
                        'city': city
                  })
                  patients.append({
                        'userId': userId,
                        'name': name,
                        'area': area,
                        'bloodGroup': bloodgroup,
                        'city': city
                  })
      except:
            patients = None
            print("Error in Get All Patients DB Call")

      return patients

#Get All Patients of Blood Group
def GetAllPatientsWithGroup(bloodGroup):
      mydb = openConnection()
      mycursor = mydb.cursor()
      patients = []
      
      try:
            mycursor.execute(getAllPatientsBloodQuery.format(bloodGroup))
            myresult = mycursor.fetchall()
            mydb.close()

            for userId, name, area, bloodgroup, city in myresult:
                  print({
                        'userId': userId,
                        'name': name,
                        'area': area,
                        'bloodGroup': bloodgroup,
                        'city': city
                  })
                  patients.append({
                        'userId': userId,
                        'name': name,
                        'area': area,
                        'bloodGroup': bloodgroup,
                        'city': city
                  })
      except:
            patients = None
            print("Error in Get All Patients DB Call")

      return patients

def GetAllPatientsWithId(id):
      mydb = openConnection()
      mycursor = mydb.cursor()
      donors = []
      
      try:
            mycursor.execute(getPatientsByIdQuery.format(id))
            myresult = mycursor.fetchall()
            
            mydb.close()
            donors = []

            for userId, name, area, bloodgroup, city in myresult:
                  donors.append({
                        'userId': userId,
                        'name': name,
                        'area': area,
                        'bloodGroup': bloodgroup,
                        'city': city
                  })

      except:
            donors = None
            print("Error in Get All Patients DB Call")            
            mydb.close()

      return donors

#Get All Donors
def GetAllDonors():
      mydb = openConnection()
      mycursor = mydb.cursor()
      donors = []
      
      try:
            mycursor.execute(getAllDonorQuery)
            myresult = mycursor.fetchall()
            
            mydb.close()
            donors = []

            for userId, name, area, bloodgroup, city in myresult:
                  donors.append({
                        'userId': userId,
                        'name': name,
                        'area': area,
                        'bloodGroup': bloodgroup,
                        'city': city
                  })

      except:
            donors = None
            print("Error in Get All Patients DB Call")            
            mydb.close()

      return donors

#Get All Donors of Blood Group
def GetAllDonorsWithGroup(bloodGroup):
      mydb = openConnection()
      mycursor = mydb.cursor()
      donors = []
      
      try:
            mycursor.execute(getAllDonorBloodQuery.format(bloodGroup))
            myresult = mycursor.fetchall()
            
            mydb.close()
            donors = []

            for userId, name, area, bloodgroup, city in myresult:
                  donors.append({
                        'userId': userId,
                        'name': name,
                        'area': area,
                        'bloodGroup': bloodgroup,
                        'city': city
                  })

      except:
            donors = None
            print("Error in Get All Patients DB Call")            
            mydb.close()

      return donors

#Get All Donors of Blood Group
def GetAllDonorsWithId(id):
      mydb = openConnection()
      mycursor = mydb.cursor()
      donors = []
      
      try:
            mycursor.execute(getDonorsByIdQuery.format(id))
            myresult = mycursor.fetchall()
            
            mydb.close()
            donors = []

            for userId, name, area, bloodgroup, city in myresult:
                  donors.append({
                        'userId': userId,
                        'name': name,
                        'area': area,
                        'bloodGroup': bloodgroup,
                        'city': city
                  })

      except:
            donors = None
            print("Error in Get All Patients DB Call")            
            mydb.close()

      return donors

# Set the current user status as patient
def SetUserStatusPatient(userId):
      mydb = openConnection()
      mycursor = mydb.cursor()

      findRecentMemberIdFormat = findLastPatientId
      mycursor.execute(findRecentMemberIdFormat)
      myresult = mycursor.fetchall()

      lastId = 0

      for id in myresult:
            lastId = id[0]

      if lastId is None:
            lastId = 0

      lastId += 1

      print("{0} is the highest patient ID".format(lastId))

      dateToday = datetime.datetime.now().strftime("%y-%m-%d")

      try: 
            finalQuery = insertPatientsQuery.format(lastId, userId, dateToday)
            print(finalQuery)
            mycursor.execute(finalQuery)
            mydb.commit()
            mydb.close()
      except mysql.connector.IntegrityError:
            print("Error received in SetUserStatusPatient 1")
            mydb.rollback()
            mydb.close()
            return False
      except Error as err:
            print("Error received in SetUserStatusPatient 2: {0}".format(err))
            mydb.rollback()
            mydb.close()
            return False
      
      return True

# Set the current user status as Donor
def SetUserStatusDonor(userId):
      mydb = openConnection()
      mycursor = mydb.cursor()

      findRecentMemberIdFormat = findLastDonorId
      mycursor.execute(findRecentMemberIdFormat)
      myresult = mycursor.fetchall()

      lastId = 0

      for id in myresult:
            lastId = id[0]
      
      if lastId is None:
            lastId = 0

      lastId += 1

      print("{0} is the highest donor ID".format(lastId))

      dateToday = datetime.datetime.now().strftime("%y-%m-%d")
      
      try:
            finalQuery = insertDonorsQuery.format(lastId, userId, dateToday)
            print(finalQuery)
            mycursor.execute(finalQuery)
            mydb.commit()
            print("Insert query committed")
            mydb.close()
      except mysql.connector.IntegrityError:
            print("Error received in SetUserStatusDonor 1")
            mydb.rollback()
            mydb.close()
            return False
      except Error as err:
            print("Error received in SetUserStatusDonor 2: {0}".format(err))
            mydb.rollback()
            mydb.close()
            return False
      
      return True

def DeletePatient(userId):
      mydb = openConnection()
      mycursor = mydb.cursor()

      try:
            finalQuery = deletePatientsQuery.format(userId)
            print(finalQuery)
            mycursor.execute(finalQuery)
            mydb.commit()
            mydb.close()
      except mysql.connector.IntegrityError:
            print("Error received in DeletePatient 1")
            mydb.rollback()
            mydb.close()
            return False
      except Error as err:
            print("Error received in DeletePatient 2: {0}".format(err))
            mydb.rollback()
            mydb.close()
            return False
      
      return True

def DeleteDonor(userId):
      mydb = openConnection()
      mycursor = mydb.cursor()

      try:
            finalQuery = deleteDonorsQuery.format(userId)
            print(finalQuery)
            mycursor.execute(finalQuery)
            mydb.commit()
            mydb.close()
      except mysql.connector.IntegrityError:
            print("Error received in DeleteDonor 1")
            mydb.rollback()
            mydb.close()
            return False
      except Error as err:
            print("Error received in DeleteDonor 2: {0}".format(err))
            mydb.rollback()
            mydb.close()
            return False
      return True
      
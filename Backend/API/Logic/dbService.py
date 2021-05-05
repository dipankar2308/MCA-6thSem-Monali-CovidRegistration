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
findLastMemberIdQuery = 'select max(memberId) from covid19donor.credentials'
insertUsersQuery = "INSERT INTO `covid19donor`.`credentials` (`userId`, `password`, `memberId`) VALUES (%s, %s, %s)"

def FindUser(username, password):
      mydb = openConnection()
      mycursor = mydb.cursor()

      userQueryFormat = finduserQueryFormat
      
      print("Query: "+ userQueryFormat.format(username,password))
      mycursor.execute(userQueryFormat.format(username,password))
      myresult = mycursor.fetchall()

      for user in myresult:
            print(user)
            return user[2]
      
      mydb.close()
      return -1

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


import mysql.connector
from Logic import Encode, Decode

mydb = mysql.connector.connect(
  host="localhost",
  user="dsutradhar",
  password="password"
)

def ReadData():
      mycursor = mydb.cursor()
      mycursor.execute("SELECT * FROM covid19donor.credentials")
      myresult = mycursor.fetchall()

      # for x in myresult:
      #       print(x)

def FindUser(username, password):
      mycursor = mydb.cursor()

      userQueryFormat = "SELECT * FROM covid19donor.credentials where userId like '{0}' and password like '{1}'"
      
      print("Query: "+ userQueryFormat.format(username,password))
      mycursor.execute(userQueryFormat.format(username,password))
      myresult = mycursor.fetchall()

      for user in myresult:
            return user[2]
      
      return -1



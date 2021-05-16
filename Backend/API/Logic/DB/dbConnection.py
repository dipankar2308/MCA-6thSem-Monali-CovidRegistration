import mysql.connector

def isProd():
      return True

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
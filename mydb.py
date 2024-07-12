import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
)
mycursor = database.cursor()

mycursor.execute("CREATE DATABASE elderco")
print("All done")
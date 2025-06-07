# Install MySQL
# link here
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector
dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password943',

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE databaseofdoom")

print("All Done, All is Well and All Shall be Well and All Manner of Things Shall be Well.")

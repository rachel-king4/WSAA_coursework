import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="password",
 database="wsaa"
)

mycursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)

mycursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
mycursor.close()
#connection.close()

import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="password",
 database="wsaa"
)

mycursor = db.cursor()
sql="select * from student where id = %s"
values = (1,)

mycursor.execute(sql, values)
result = mycursor.fetchall()
for x in result:
 print(x)
mycursor.close()
#connection.close()
import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="password",
 #user="datarep", # this is the user name on my mac
 #passwd="password" # for my mac
 database="wsaa"
)

mycursor = db.cursor()
sql="delete from student where id = %s"
values = (1,)

mycursor.execute(sql, values)

db.commit()
print("delete done")
mycursor.close()
#connection.close()

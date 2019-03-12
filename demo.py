print("hello")
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="test")
mycursor=mydb.cursor()
mycursor.execute("select * from bang;")
result =  mycursor.fetchall()
for i in result:
    print(i)
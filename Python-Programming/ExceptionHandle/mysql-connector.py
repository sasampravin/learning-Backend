import mysql.connector
try:
    con=mysql.connector.Connection(host='localhost',user='root',password='root')
    print('type of con is : ',type(con))
    print('python program got connection from mysql database')
    cur=con.cursor()
    print('type of cur is : ',type(cur))
    print('python program created cursor object')

except mysql.connector.DatabaseError as db:
    print('problam in MySQL: ',db)

import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="dbpython")

query = db.cursor()

loop = 'true'
while(loop == 'true'):
    username = raw_input("Username: ")
    password = raw_input("password : ")
    if(query.execute("SELECT * FROM 'test1' where 'username'='" + username + "' AND 'password'='" + password + "'")):
        db.commit()
        print ("logged in")
    else:
        db.commit()
        print ("FAil")

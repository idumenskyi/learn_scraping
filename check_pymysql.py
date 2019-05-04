import pymysql

def conn():
    mydb=pymysql.Connect('localhost','root','2202414','mysql',autocommit=True)
    return mydb.cursor()

def db_exe(query,c):
    try:
        if c.connection:
            print("connection exists")
            c.execute(query)
            return c.fetchall()
        else:
            print("trying to reconnect")
            c=conn()
    except Exception as e:
        return str(e)

dbc=conn()
print(db_exe("select * from users",dbc))

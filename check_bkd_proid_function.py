import mysql.connector as mc

db = mc.connect(
        host="localhost",
        user="root",
        passwd="378400",
        database="sboutique"
    )
cursor = db.cursor()
print("Database connection successful")

def check():
    showid="select pro_id from products"
    cursor.execute(showid)
    result=cursor.fetchall()
    list_id=[]
    for i in result:
        list_id.append(i[0])
    return list_id

print(check())
db.close()
    

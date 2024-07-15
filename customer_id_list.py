import mysql.connector as mc

db = mc.connect(
        host="localhost",
        user="root",
        passwd="378400",
        database="sboutique"
    )
cursor = db.cursor()

def check():
    #make a list of customers id
    showid = "SELECT cust_id FROM customer"
    cursor.execute(showid)
    result = cursor.fetchall()
    list_id = []
    for i in result:
        list_id.append(i[0])
    return list_id

#Properly Working


    

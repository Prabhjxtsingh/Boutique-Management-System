import mysql.connector as mc
db = mc.connect(
    host= 'localhost',
    user = 'root',
    password = '378400',
    database = 'sboutique'
)
cursor = db.cursor()

#function that ID of a costumer exist or not 
def check():
    show_id = 'select cust_id from customer'
    cursor.execute(show_id)
    print("Customer's ID are fetched")
    result = cursor.fetchall()
    list_ID = []
    for i in result:
        list_ID.append(i[0])

    return list_ID

check()
print("List appended")

import mysql.connector as  mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="378400",
    database="sboutique"
)

cursor=db.cursor()
def get_bkd_pro(cust_id):
    showbkd_products=f'select bkd_pro from customer where cust_id={cust_id}'
    cursor.execute(showbkd_products)
    #return the bkd_pro from customer
    showbkd_products="select bkd_pro from customer where cust_id=%s"
    cursor.execute(showbkd_products,(cust_id,))
    result=cursor.fetchone()
    booked_pro=result[0]
    return booked_pro

#print(get_bkd_pro(1))
#properly Working

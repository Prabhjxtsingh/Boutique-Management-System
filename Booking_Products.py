#import Check_function as ch
#import Customer_Account as ca
import mysql.connector as mc
db = mc.connect(
    host= 'localhost',
    user = 'root',
    password = '378400',
    database = 'sboutique'
)
cursor = db.cursor()

# To select all booked products of  a given customer from the table
def get_bkd_pro(custid):
    qry = 'select bkd_pro from customer where cust_id=%s;'
    cursor.execute(qry, (custid,))
    bp = cursor.fetchone()
    bkd_pro = bp[0]
    return bkd_pro
print(get_bkd_pro(1))

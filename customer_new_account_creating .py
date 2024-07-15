import customer_id_list as cil
import mysql.connector as  mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="378400",
    database="sboutique"
)

cursor=db.cursor()

def cust_acc():
    ask="Y"
    # this list_of_id stores the list of customers id by using check function from customer_id_list
    list_of_id=cil.check()
    while ask in "yY":
        customer_id=int(input("Enter Your Customer ID: "))
        #using the list if exist then simply put print command of existance or if not then take a new inputs
        if customer_id  in list_of_id:
            print("This customer is already existed. Try creating new one")
        else:
            customer_nam = input('First Name : ')
            customer_lnam = input('Last Name : ')
            customer_phno = input('Phone Number : ')
            customer_adrs = input('Your Address : ')
            c_det = (customer_id, customer_nam, customer_lnam, customer_phno, customer_adrs)
            
            
            insertQuery="insert into customer( cust_id,c_nam,c_lnam,c_phno,c_adrs) values(%s,%s,%s,%s,%s)"
            val=c_det
            cursor.execute(insertQuery,val)
            db.commit()
            print('Customer details entered')
            ask = input('Do you want to continue (Y/N) ')
            if ask not in ('Yy'):
                break

#Properly Working
            
            

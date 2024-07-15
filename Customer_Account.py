import Check_function as ch
import Booking_Products as BP
import mysql.connector as mc
db = mc.connect(
    host= 'localhost',
    user = 'root',
    password = '378400',
    database = 'sboutique'
)

cursor = db.cursor()
print(' $$ database connection took succesfull $$ ')
#function to create a new account for the customer
def cust_ac():
    ask = 'Y'
    list_IDs = ch.check()
    print(list_IDs)
    while ask in 'yY':
        custid = int(input('Enter your customer id .....   '))

        if custid in list_IDs:
            print('This Custoemr Id already exists.... \n Try creating a new one')
        else:
            # Tuple to contain details of the customer
            c_det = ()
            cnam = input('First Name : ')
            clnam = input('Last Name : ')
            cphno = input('Phone Number : ')
            cadrs = input('Your Address : ')
            c_det = (custid, cnam, clnam, cphno, cadrs)

# Values inserted in the table and default NULL value are provided for booked product at the time of creation  of customer account 

            insertion_query = 'INSERT INTO customer (cust_id, c_nam, c_lnam, c_phno, c_adrs) VALUES (%s, %s, %s, %s, %s)'
            insertion_values = c_det # values of the columns of customer table
            cursor.execute(insertion_query , insertion_values)
            db.commit()
            print('Customer details entered...')
            ask = input('Do you want to continue ( Y / N )....   ')
            if ask not in ('Yy'):

                break
            
cust_ac()
db.close()

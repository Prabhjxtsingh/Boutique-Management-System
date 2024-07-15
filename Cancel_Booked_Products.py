import mysql.connector as mc
import Booked_products_from_customer as bpfc
db = mc.connect(
        host="localhost",
        user="root",
        passwd="378400",
        database="sboutique"
    )
cursor = db.cursor()

def cancel(b):
    # get details of products which customers booked  
    bookedproduct=bpfc.get_bkd_pro(b)
    print("Your Booking :",bookedproduct)
    #check whether the booked product is None as it exists or not
    if bookedproduct is None or bookedproduct==" ":
        print("You Have No Booking To Cancel")
    else:
        #if booked products are there then cancel either all or the given specific product
        cancelproduct=input("To cancel all Product Go for option : A or a \nTo cancel specific product Enter Product Code")
        if cancelproduct in  "Aa":
            query="Update customer set bkd_pro=Null where cust_id=%s"
            cursor.execute(query,(b,))
            db.commit()
            print("All Booking Cancelled")
        elif cancelproduct in bookedproduct:
            #x is the list of all booked products using 0 for starting and -1 to tell ending and also split them
            x=(bookedproduct[0:-1]).split('_')
            # this pre define function helps to remove that specific product
            x.remove(cancelproduct)
            updated_product = ''
            # Again concatenate each product ID in the list to store in the table
            for i in x:
                updated_product = updated_product+i+'_'
            # Updated the booking product in customer after deletion
            query = 'update customer set bkd_pro=%s where cust_id=%s'
            val = (updated_product,b)
            cursor.execute(query, val)
            db.commit()
            print('Booking Cancelled !')
            
#cancel(1)
#properly Working
    
    

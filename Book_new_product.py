import mysql.connector as mc
import products_id_list as pil
import Booked_products_from_customer as bpfc

db = mc.connect(
        host="localhost",
        user="root",
        passwd="378400",
        database="sboutique"
    )
cursor = db.cursor()

def booking(m):
    # Check product to be booked exists or not
    # use function of products_id_list which is check() to get the list of products
    productlist=pil.check()
    print("List of Various Products")
    for i in productlist:
        print("Product ID:",i)
    print("\n")
    pro_id = input('Enter the product id to book products :  ')
    # use function of products_id_list which is check() to check whether the given pro_id is their in product id list
    if pro_id in productlist:
        # use function get_bkd_pro from Booked_product_from_customer as bpfc to fetch the product id from specific customer
        productid=bpfc.get_bkd_pro(m)
        if productid is None or productid==' ':
            # updating the bkd_pro with the pro_id which we input
            enterproidquery="update customer set bkd_pro=%s where cust_id=%s "
            #pro_id which is input is now added 
            val=(pro_id+"_",m)
            cursor.execute(enterproidquery,val)
            db.commit()
            print("Your Product is booked")
        else:
            # Suppose if there is already any product book then we concatenaate the other product with it
            #make a new variable in which concatenate the previous id with newid
            newproductid=productid+pro_id
            query2 = 'update customer set bkd_pro=%s where cust_id=%s;'
            # val2 is the new value containing all booked products to be stored in the column
            val2 = (newproductid+'_', m)
            cursor.execute(query2, val2)
            db.commit()
            print('Your Product is booked !!')
    else:
        print('This product does not exists.Please write the correct product id!')
    
#Working Properly
        
    
    

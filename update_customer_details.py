import mysql.connector as  mc
import view_customer_details as vcd
import view_updated_customer_details as vucd
db=mc.connect(
    host="localhost",
    user="root",
    passwd="378400",
    database="sboutique"
)

cursor=db.cursor()
#updating the customer details
def updation(a):
    #use printdata function from view_customer_details as vcd to print existing table
    vcd.printdata(a)
    data="""select cust_id, c_nam,c_lnam,c_phno,c_adrs from customer where cust_id =%s"""
    cursor.execute(data,(a,))            
    c_list=cursor.fetchone()
    #make global variable and add the respective values
    updatedname,updateLastname,updatephone,updateaddress=c_list[1],c_list[2],c_list[3],c_list[4]
    while True:
        print("Please make a choice to update the existing data")
        print("1: Update Your Name\n2: Update Your Last Name\n3: Update Your Phone_no.\n4: Update Your Address\n5: Exit")
        option=int(input("Enter the choice: " ))
        if option==1:
            updatedname=input("Enter the New Name: ")
        elif option==2:
            updateLastname=input("Enter the New Last Name: ")
        elif option==3:
            updatephone=input("Enter the New Phone Number: ")
        elif option==4:
            updateaddress=input("Enter the New Address: ")
        elif option==5:
            break
        else:
            print("Input Option is Wrong")
    update_query="""update customer set c_nam=%s,c_lnam=%s,c_phno=%s,c_adrs=%s where cust_id=%s """    
    value=(updatedname,updateLastname,updatephone,updateaddress,a)
    cursor.execute(update_query,value)   
    db.commit()
    print("Updated Values")
    #use printupdateddata function from view_updated_customer_details as vucd to print updated data of customer
    vucd.printupdateddata(a)

#updation(1)
#Working Properly

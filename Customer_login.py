
import mysql.connector as mc
import customer_id_list as cil
import View_booking_details as vbd
import Book_new_product as bep
import update_customer_details as ucd
import Cancel_Booked_Products as cbp

def sign_in():
    ask=int(input("Enter the Customer Id to sign in: "))
    # get list of id from check function
    List_of_id=cil.check()  
    #check whether the input customer id is in that list of id
    if ask in List_of_id:
        #if it is there then
        while True:
            #options
            print("""Do You want to.....\n1:View Bookings\n2:Book a product\n3:Update Self Details\n4:Cancel Booked Product\n5:Exit""")
            choice=int(input("Enter Choice: "))
            
            #first choice for to see booking
            if choice==1:
                #get detail about booking products using view_booking_details as vbd
                vbd.viewbookingdetails(ask)
                
    
                
            #second choice for to book a new product
            elif choice==2:
                #use function booking from Book_new_product as bep
                bep.booking(ask)
                
                
            # third Choice for updating the Customer details 
            elif choice==3:
                # use updation function from updated_customer_details as ucd 
                ucd.updation(ask)
            #fourth choice for cancelling the product
            elif choice==4:
                #use cancel function from Cancel_Booked_Products as cbp 
                cbp.cancel(ask)
    
            #Fith to exit from This Program
            elif choice==5:
                print("Successfully Logged Out")
                break
            else:
                print("Enter valid Choice")
            
            
sign_in()

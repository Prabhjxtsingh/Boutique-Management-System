import mysql.connector as mc
import Booked_products_from_customer as bpfc

def connect_db():
    db = mc.connect(
        host="localhost",
        user="root",
        passwd="378400",
        database="sboutique"
    )
    return db

def view_booking_details(n):
    db = connect_db()
    cursor = db.cursor()
    booked_details = bpfc.get_bkd_pro(n)
    if not booked_details:
        print('You have not booked products yet.')
    else:
        all_products = booked_details.split('_')
        print('Booked products:')
        for product in all_products:
            print(product)
    cursor.close()
    db.close()

# Test the function with a sample input
view_booking_details(1)

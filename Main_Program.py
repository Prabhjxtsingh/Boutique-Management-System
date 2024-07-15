import mysql.connector

# Establish MySQL connection
mycon = mysql.connector.connect(
    host='localhost', user='root',
    password='378400', database='sboutique')

# Create MySQL cursor
mycur = mycon.cursor()

# Function to provide blank spaces in the output
def space():
    print()

# Function to check if a customer of a given ID exists
def check():
    qry = 'SELECT cust_id FROM customer;'
    mycur.execute(qry)
    # Fetch all customer IDs into a list
    d = mycur.fetchall()
    list_of_ids = [ids[0] for ids in d]
    return list_of_ids

# Function to create a new customer account
def cust_ac():
    list_of_ids = check()
    ask = 'Y'
    while ask in 'yY':
        custid = int(input('Enter your customer id: '))
        if custid in list_of_ids:
            print('This Customer ID already exists. Try creating a new one.')
        else:
            c_det = ()
            cnam = input('First Name: ')
            clnam = input('Last Name: ')
            cphno = input('Phone Number: ')
            cadrs = input('Your Address: ')
            c_det = (custid, cnam, clnam, cphno, cadrs)
            
            qry = 'INSERT INTO customer VALUES (%s, %s, %s, %s, %s, NULL);'
            val = c_det
            
            mycur.execute(qry, val)
            mycon.commit()
            print('Customer details entered.')
            ask = input('Do you want to continue (Y/N)? ')
            if ask not in ('Yy'):
                space()
                break

# Function to retrieve booked products for a customer
def get_bkd_pro(cust_id):
    qry = 'SELECT bkd_pro FROM customer WHERE cust_id=%s;'
    mycur.execute(qry, (cust_id,))
    bp = mycur.fetchone()
    bkd_pro = bp[0] if bp else None
    return bkd_pro

# Function for customer sign-in and interaction
def sign_in():
    try:
        ask = int(input('Enter customer ID to sign in: '))
        list_of_ids = check()
        if ask in list_of_ids:
            while True:
                print('''Do you want to:
                         1) View Bookings
                         2) Book a Product
                         3) Update Self Details
                         4) Cancel Booked Products
                         Enter 'back' to exit''')
                ccc = input('Enter choice: ')
                
                if ccc == '1':
                    s = get_bkd_pro(ask)
                    if s is None or s.strip() == '':
                        print('You have not booked any products yet.')
                    else:
                        d = s.split('_')
                        print('Booked products:')
                        for bkditems in d:
                            print(bkditems)

                elif ccc == '2':
                    qry = 'SELECT pro_id FROM products;'
                    mycur.execute(qry)
                    pro_list = [i[0] for i in mycur.fetchall()]

                    pro_id = input('Enter the product ID to book products: ')
                    if pro_id in pro_list:
                        qry = 'SELECT bkd_pro FROM customer WHERE cust_id=%s;'
                        mycur.execute(qry, (ask,))
                        pr = mycur.fetchone()
                        prl = pr[0] if pr else None
                        
                        if prl is None or prl.strip() == '':
                            qry = 'UPDATE customer SET bkd_pro=%s WHERE cust_id=%s;'
                            val = (pro_id + '_', ask)
                            mycur.execute(qry, val)
                            mycon.commit()
                            print('Your product is booked!')
                        else:
                            prl1 = prl + pro_id
                            qry = 'UPDATE customer SET bkd_pro=%s WHERE cust_id=%s;'
                            val2 = (prl1 + '_', ask)
                            mycur.execute(qry, val2)
                            mycon.commit()
                            print('Your product is booked!')

                    else:
                        print('This product does not exist. Please enter the correct product ID.')

                elif ccc == '3':
                    qry = 'SELECT cust_id, c_nam, c_lnam, c_phno, c_adrs FROM customer WHERE cust_id=%s'
                    mycur.execute(qry, (ask,))
                    clist = mycur.fetchone()
                    flds = ['Name', 'Last Name', 'Ph.No', 'Address']
                    dic = {}

                    print("Your existing record is:")
                    for i in range(4):
                        dic[flds[i]] = clist[i+1]
                        print(i+1, flds[i], ':', clist[i+1])

                    for i in range(len(clist)):
                        updtc = int(input('Enter choice to update: '))
                        upval = input('Enter ' + flds[updtc-1] + ': ')
                        dic[flds[updtc-1]] = upval
                        yn = input('Do you want to update other details? (y/n): ')
                        if yn in 'Nn':
                            break

                    qry = 'UPDATE customer SET c_nam=%s, c_lnam=%s, c_phno=%s, c_adrs=%s WHERE cust_id=%s;'
                    updtl = tuple(dic.values()) + (ask,)
                    val = updtl
                    mycur.execute(qry, val)
                    mycon.commit()
                    print('Your details are updated.')

                elif ccc == '4':
                    try:
                        bkd_pro = get_bkd_pro(ask)
                        print('Your Bookings:\n', bkd_pro)
                        if bkd_pro is None or bkd_pro.strip() == '':
                            print('You have no bookings to cancel.')
                        else:
                            cw = input("To cancel all products, enter 'A'\nOr enter the product code to cancel: ")
                            if cw in 'Aa':
                                qry = 'UPDATE customer SET bkd_pro=NULL WHERE cust_id=%s;'
                                mycur.execute(qry, (ask,))
                                mycon.commit()
                                print('All bookings deleted.')
                            elif cw in bkd_pro:
                                x = (bkd_pro[0:-1]).split('_')
                                x.remove(cw)
                                updt_pro = ''
                                for item in x:
                                    updt_pro = updt_pro + item + '_'
                                qry = 'UPDATE customer SET bkd_pro=%s WHERE cust_id=%s;'
                                val = (updt_pro, ask)
                                mycur.execute(qry, val)
                                mycon.commit()
                                print('Booking Cancelled!')
                    except Exception:
                        print('Some problem in updating details. Try again.')

                elif ccc.lower() == 'back':
                    print("Successfully logged out.")
                    space()
                    break

        else:
            print('This account does not exist.')
    
    except Exception:
        print('Some error occurred. Try Again.')

# Function to view all products
def view_pro():
    qry = 'SELECT * FROM products;'
    mycur.execute(qry)
    d = mycur.fetchall()
    print('_'*80)
    print("{:<17} {:<22} {:<23} {:<19}".format(
        'Product ID', 'Product Name', 'Price', 'Stock'))
    print('_'*80)
    for k, v in d:
        print("{:<17} {:<22} {:<23} {:<19}".format(k, *v))
    print('_'*80)

# Function to add a new product
def addpro():
    view_pro()
    n = int(input('Enter number of items to insert: '))
    for j in range(n):
        t = ()
        pronum = input("Product No.: ")
        proid = input('Product ID: ')
        pprice = int(input('Price: '))
        pstk = int(input('Stock: '))
        t = (pronum, proid, pprice, pstk)
        qry = 'INSERT INTO products VALUES (%s, %s, %s, %s);'
        val = t
        mycur.execute(qry, val)
        mycon.commit()
        print("Product Added.")

# Function to delete a product
def delpro():
    view_pro()
    delt = input("Enter ID of product to be deleted: ")
    qry = 'DELETE FROM products WHERE pro_id=%s;'
    mycur.execute(qry, (delt,))
    mycon.commit()
    print("Product deleted.")

# Function for employee sign-in and actions
def emp_sign_in():
    try:
        ask = input('Enter ID to sign in to the account: ')
        qry = 'SELECT emp_id FROM employee;'
        mycur.execute(qry)
        lis = [i[0] for i in mycur.fetchall()]
        
        if ask not in lis:
            print('Enter the correct ID.')
        else:
            while True:
                space()
                ccc = input('''1. Update delivered records
                             2. Add a New Product
                             3. Delete a Product
                             Enter 'Back' to logout: ''')
                if ccc == '1':
                    cust_id = input('Enter customer ID: ')
                    bkd_pro = get_bkd_pro(cust_id)
                    
                    if bkd_pro is None or bkd_pro.strip() == '':
                        print('This customer has no bookings.')
                    else:
                        print('All bookings:', bkd_pro)
                        pro_id = input('Enter product code to remove the delivered product: ')
                        
                        if pro_id in bkd_pro:
                            x = (bkd_pro[0:-1]).split('_')
                            x.remove(pro_id)
                            updt_pro = ''
                            
                            for item in x:
                                updt_pro = updt_pro + item + '_'
                            qry = 'UPDATE customer SET bkd_pro=%s WHERE cust_id=%s;'
                            val = (updt_pro, cust_id)
                            mycur.execute(qry, val)
                            mycon.commit()
                            print('Updated records.')

                        else:
                            print('Enter the correct product ID.')
                    
                elif ccc == '2':
                    addpro()

                elif ccc == '3':
                    delpro()

                elif ccc.lower() == 'back':
                    print('Logged out successfully.')
                    break
    except Exception:
        print('Some error in update. Try again.')

# Function for employer actions
def employer():
    while True:
        space()
        print('1. To view product details')
        print('2. Add an employee')
        print('Enter "back" to exit')
        print()
        try:
            enq = int(input("Select a number: "))
            if enq == 1:
                view_pro()
            elif enq == 2:
                addemp()
            elif enq == 'back':
                break
            else:
                print('Invalid input. Please try again.')
        
        except ValueError:
            print('Invalid input. Please try again.')

# Function to add a new employee
def addemp():
    try:
        empn = int(input('Enter employee ID: '))
        if empn in check():
            print('This employee ID already exists.')
        else:
            q = ()
            q = (empn, input('First Name: '), input('Last Name: '), input('Phone Number: '), input('Enter your address: '))
            qry = 'INSERT INTO employee VALUES (%s, %s, %s, %s, %s);'
            val = q
            mycur.execute(qry, val)
            mycon.commit()
            print('Employee has been added.')
            
    except Exception:
        print('Some error occurred. Try again.')

# Main Application Loop
while True:
    print('1. Customer')
    print('2. Employee')
    print('3. Employer')
    print('4. Exit')
    c = input('Enter your choice: ')
    
    if c == '1':
        sign_in()
    
    elif c == '2':
        emp_sign_in()
    
    elif c == '3':
        employer()
    
    elif c == '4':
        print('Successfully logged out.')
        break
    
    else:
        print('Invalid input. Please try again.')

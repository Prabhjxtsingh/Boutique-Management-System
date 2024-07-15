import mysql.connector as  mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="378400",
    database="sboutique"
)

cursor=db.cursor()
print("All Database")
showdatabase="Show Databases"
cursor.execute(showdatabase)
result=cursor.fetchall()
for i in result:
    print(i)

print("\n")  
print("All Tables")
showtables="Show Tables"
cursor.execute(showtables)
result=cursor.fetchall()
for i in result:
    print(i)
    
print("\n")  
print(" Show Table Products")
showproducts="Select * from products"
cursor.execute(showproducts)
result=cursor.fetchall()
for i in result:
    print(i)

print("\n")  
print(" Show Table Customers")
showcustomer="Select * from customer"
cursor.execute(showcustomer)
result=cursor.fetchall()
for i in result:
    print(i)
    
print("\n")  
print(" Show Table Employees")
showemployee="Select * from employee"
cursor.execute(showemployee)
result=cursor.fetchall()
for i in result:
    print(i)

print("\n")  
print(" Describe Table Customers")
describecustomers="desc customer"
cursor.execute(describecustomers)
result=cursor.fetchall()
for i in result:
    print(i)
    
print("\n")  
print("Describe Table Products")
describeproducts="desc products"
cursor.execute(describeproducts)
result=cursor.fetchall()
for i in result:
    print(i)
    
print("\n")  
print("Describe Table Employees")
describeemployees="desc employee"
cursor.execute(describeemployees)
result=cursor.fetchall()
for i in result:
    print(i)

db.close()

#properly Working

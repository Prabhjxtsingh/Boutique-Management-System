import mysql.connector as  mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="378400",
    database="sboutique"
)

cursor=db.cursor()
'''
#Create database
database_name="create database sboutique"

cursor.execute(database_name)
print("Database created")
'''


#creating table (customer)
tablecustomer="""create table customer (
    cust_id int PRIMARY KEY,
    c_nam varchar(30) not null,
    c_lnam varchar(30) not null,
    c_phno varchar(10) not null,
    c_adrs varchar(50) not null,
    bkd_pro varchar(40))
"""

cursor.execute(tablecustomer)
print("table customer created")

#creating table(employee)
tableemployee="""create table employee (
    emp_id int PRIMARY KEY,
    e_nam varchar(30) not null,
    e_lnam varchar(30) not null,
    e_phno varchar(10) not null,
    e_adrs varchar(30) not null)"""

cursor.execute(tableemployee)
print("table employee created")

#creating table (products)
tableproducts="""create table products (
    pro_num varchar(5) not null,
    pro_id varchar(50)  PRIMARY KEY,
    pro_price int not null,
    pro_stk int not null)"""

cursor.execute(tableproducts)
print("table products created")

# inserting values in products

insertingproducts="""INSERT INTO products(pro_num,pro_id,pro_price,pro_stk) VALUES(%s,%s,%s,%s)"""
values=[('1','KWPTP25',330,18),
('2','KWPTP30',450,30),
('3','KWPTP45',650,20),
('4','SSST025',850,10),
('5','SSST030',350,12)]

cursor.executemany(insertingproducts,values)
db.commit()
print("Values Inserted")

db.close()

#properly working

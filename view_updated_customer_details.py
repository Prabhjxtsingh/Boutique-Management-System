import mysql.connector as  mc
db=mc.connect(
    host="localhost",
    user="root",
    passwd="378400",
    database="sboutique"
)

cursor=db.cursor()
# return the updated detail of the customer 
def printupdateddata(a):
    data="""select cust_id, c_nam,c_lnam,c_phno,c_adrs from customer where cust_id =%s"""
    cursor.execute(data,(a,))            
    c_list=cursor.fetchone()
    column_name=["Customer_id: ","Name: ","Last Name: ","Phone_no.: ","Address: "]
    dic={}
    print("Your Updated Data ")
    for i in range(len(column_name)):
        dic[column_name[i]]=c_list[i]
        print(i+1," ",column_name[i]," ",c_list[i])

#printupdateddata(1)
#Working Properly

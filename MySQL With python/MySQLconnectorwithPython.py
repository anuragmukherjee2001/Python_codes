import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user = "aptech",
    password ="cmc",
    database = "aptech"

)
mycursor = mydb.cursor()
sql = "INSERT INFO laptop(Laptop_id,Model1_name,price)VALUES(%s,%s,%s)"
val = (145,"DELL",32000)
mycursor.execute(sql,val)
mydb.comit()
print(mycursor.rowcount,"record inserted")
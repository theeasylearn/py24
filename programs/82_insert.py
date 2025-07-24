#example of insert record into mysql table
#table : category
#fields : id(PK & auto_increment),name,detail,status,created_at (default current_timestamp)
import dbconnction as con #here con is nick name for database

#create cursor type object
mycursor = con.database.cursor()

#create sql variable(string) to store sql command(insert/update/delete/select any sql command in this case insert)
sql = "insert into category (name,detail,status) values (%s,%s,%s)"
#%s is called placeholder 

#create list(array) size of the list must same no of placeholder 
name = input("Enter category name")
detail = input("Enter category detail")
status = int(input("enter category status (1= live,0= not live)"))
data = [name,detail,status]
#execute sql command using sql and data 
mycursor.execute(sql,data)

#save changes into database
con.database.commit()

print(mycursor.rowcount," Category inserted ")
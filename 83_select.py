#example of fetch records from mysql table
#table : category
#fields : id(PK & auto_increment),name,detail,status,created_at (default current_timestamp)
import dbconnction as con #here con is nick name for database

#create cursor type object
mycursor = con.database.cursor()

#create sql variable(string) to store sql command(insert/update/delete/select any sql command in this case select)
sql = "select * from category order by id desc"
#%s is called placeholder 

#run sql command 
mycursor.execute(sql) 

#fetch one row 
# single_record = mycursor.fetchone()
# print(single_record)

#fetch all row 
table = mycursor.fetchall()
print(table)
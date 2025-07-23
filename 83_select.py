#example of fetch records from mysql table
#table : category
#fields : id(PK & auto_increment),name,detail,status,created_at (default current_timestamp)
import dbconnction as con #here con is nick name for database

#create cursor type object
mycursor = con.database.cursor(dictionary=True)

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
# print(table)
print("_"*115)
print(f"{'id':6}{'name':32}{'detail':48}{'status':10}{'created_at':12}")
print("_"*115)
for row in table:
    if row['status'] == 0:
        row['status'] = 'Not Live'
    else: 
        row['status'] = 'Live'
    created_at = row['created_at'].strftime('%d-%m-%Y %H:%M:%S')
    print(f"{row['id']:2}{'':4}{row['name']:32}{row['detail']:48}{row['status']:10}{created_at:18}")
#how to update row in table 
import dbconnction as con

id = int(input("enter category id to update category"))
name = input("enter updated category name")
detail = input("enter updated category detail")
status = int(input("enter updated category status"))

mycursor = con.database.cursor()

sql = "update category set name=%s, detail=%s,status=%s where id=%s"
data = [name,detail,status,id]
mycursor.execute(sql,data)
con.database.commit()
if mycursor.rowcount==0:
    print("no category found")
else:
    print("category has been updated successfully")
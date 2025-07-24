import dbconnction as con 
#how to delete row in table
id = int(input("enter category id to delete category"))
mycursor = con.database.cursor()
sql = "delete from category where id=%s"
data = [id]
mycursor.execute(sql,data)
con.database.commit()
if mycursor.rowcount == 0:
    print("no category found")
else:
    print("category has been deleted...")
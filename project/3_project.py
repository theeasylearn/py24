import dbconnection as con
#menu drive program
def getBookDetail():
    title = input("Enter book name")
    author = input("Enter author name")
    year_published = int(input("Enter publish year"))
    genre = input("Enter book genre")
    status = int(input("book status (1 = owned, 2 = borrowed)"))
    return title,author,genre,year_published,status 
def display(tables):
    print(f"{'id':10}{'title':32}{'author':32}{'generation':24}{'year_published':24}{'status':10}")
    print("_"*135)
    for row in tables:
        if row['status'] == 1:
            row['status'] = "owned"
        else:
            row['status'] = "borrowed"    
        print(f"{row['id']:2}{'':8}{row['title']:32}{row['author']:32}{row['genre']:24}{row['year_published']:4}{'':20}{row['status']:10}")
print("Press 1 to insert new book")
print("Press 2 to update book")
print("Press 3 to delete book")
print("Press 4 to display all book")
print("Press 5 to search book by title")
print("Press 6 to search book by author")
print("Press 7 to search book by generation")
print("Press 8 to change flag")
print("Press 0 to exit")
while True:
    try:
        choice = int(input("what is your choice"))
        if choice==1:
            # accept bookname, author, genre, year_published, status from user 
            tuple = getBookDetail()
            sql = "insert into books (title,author,genre,year_published,status) values (%s,%s,%s,%s,%s)"
            data = [tuple[0],tuple[1],tuple[2],tuple[3],tuple[4]]
            isSuccess = con.RunQuery(sql,data)
            if isSuccess==True:
                print("Book inserted successfully")
        elif choice==2:
            print("I will update book")
            bookid = int(input("Enter book id to update"))
            tuple = getBookDetail()
            sql = "update books set title=%s,author=%s,genre=%s,year_published=%s,status=%s where id=%s"
            data = [tuple[0],tuple[1],tuple[2],tuple[3],tuple[4],bookid]
            isSuccess = con.RunQuery(sql,data)
            if isSuccess==True:
                print("Book updated successfully")
        elif choice==3:
            print("I will delete book")
            bookid = int(input("Enter book id to delete book"))
            sql = "delete from books where id=%s"
            data = [bookid]
            isSuccess = con.RunQuery(sql,data)
            if isSuccess==True:
                print("Book deleted successfully")
        elif choice==4:
            sql = "select * from books order by id desc"
            tables = con.fetchTable(sql)
            display(tables)    
        elif choice==5:
            title = input("Enter book name")
            sql = "select * from books where title like %s"
            data = ['%' + title + '%'] 
            tables = con.fetchTable(sql,data)
            display(tables)
        elif choice==6:
            author = input("Enter author name")
            sql = "select * from books where author like %s"
            data = ['%' + author + '%'] 
            tables = con.fetchTable(sql,data)
            display(tables)
        elif choice==7:
            print("I will search book using generation")
            genre = input("Enter book generation")
            sql = "select * from books where genre like %s"
            data = ['%' + genre + '%'] 
            tables = con.fetchTable(sql,data)
            display(tables)
            
        elif choice==8:
            print("I will change flag")
            bookid = int(input("Enter book id to update flag"))
            status = int(input("enter new status for book (1 = owned, 2 = borrowed)"))
            sql = "update books set status=%s where id=%s"
            data = [status,bookid]
            isSuccess = con.RunQuery(sql,data)
            if isSuccess==True:
                print("Book updated successfully")
        elif choice==0:
            print("Good bye.");
            break
        else:
            print("invalid choice")
    except ValueError as e:
        print("invalid input, only numbers are allowed")
print("End of program")

import dbconnection as con
#menu drive program
def getBookDetail():
    title = input("Enter book name")
    author = input("Enter author name")
    year_published = int(input("Enter publish year"))
    genre = input("Enter book genre")
    status = int(input("book status (1 = owned, 2 = borrowed)"))
    return title,author,genre,year_published,status 
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
            print("I will display all book")
        elif choice==5:
            print("I will search book using title")
        elif choice==6:
            print("I will search book using author")
        elif choice==7:
            print("I will search book using generation")
        elif choice==8:
            print("I will change flag")
        elif choice==0:
            print("Good bye.");
            break
        else:
            print("invalid choice")
    except ValueError as e:
        print("invalid input, only numbers are allowed")
print("End of program")

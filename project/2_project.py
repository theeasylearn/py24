import dbconnection as con
#menu drive program
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
            sql = "insert into book (title,author,genre,year_published,ststus) values (%s,%s,%s,%s,%s)"
            data = ['Rich dad poor dad','Robert','finanace',2000,1]
            
        elif choice==2:
            print("I will update book")
        elif choice==3:
            print("I will delete book")
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

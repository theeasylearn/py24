'''
    write a program to findout whether person is eligible to apply for civil service exam  or not from given age as per below criteria 
        person age is above 18 and less 36 then he/she can apply for civil service 
        otherwise person can not apply for civil service 
    steps 
        1) create variable age & accept input from user 
        2) check age>18 as well as age<36 then 
            print person can apply for civil service 
        3) else 
            print person is not eligible for civil service 
'''
age = int(input("Enter your age"))
if age>18 and age<36:
    print("person can apply for civil service ")
else:
    print("person is not eligible for civil service")
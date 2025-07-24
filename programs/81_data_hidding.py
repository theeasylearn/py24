class Account:
    __balance = 0
    def __init__(self,name,balance):
        self.name = name  #public instance variable
        self.__balance = balance #private instance variable
    def updateBalance(self,amount):
        self.__balance += amount
    def display(self):
        print(f"Name = {self.name} Balance = {self.__balance}")

b1 = Account("Ankit Patel",10000)
b1.display()
b1.updateBalance(99)
b1.display()
b1.updateBalance(-99)
b1.display()
b1.__balance = 0 #is ignored because __balance is private variable
b1.display()
#to access private variable we given object._className__private_variable_name 
print(b1._Account__balance)
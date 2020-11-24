
import os

class User:
    #Define the attributes of the class
    name = "mike"
    email = "mj@mj.me"
    password = "1234"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

# Child class
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "0000"

#This is the same method in the parent class "User".
#The difference is that instead of using entry_password, we're using entry_pin

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}".format(entry_name))
        else:
            print("Your pin or email is incorrect")

# Child class 2
class Student(User):
    nickname = "tweak"
    mail = "tw@eak.com"
    smoke = "weed"

#This is the same method in the parent class "User".
#The difference is that instead of using entry_name, we're using entry_nickname

    def getLoginInfo(self):
        entry_nick = input("Enter your nickname: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_nick == self.nickname and entry_email == self.mail):
            print("Welcome back, {}".format(entry_nick))
        else:
            print("Your pin or email is incorrect")

#The following code invokes the methods inside each class for User, Employee, and Student
customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

wastoid = Student()
wastoid.getLoginInfo()

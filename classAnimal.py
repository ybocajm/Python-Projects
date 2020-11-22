
import os

class Whale:
    #Define the attributes of the class
    type = "No type"
    size = "varies"
    weight = "large"
    habitat = "ocean"

    def _init__(self, type, size, weight, habitat):
        self.type = type
        self.size = size
        self.weight = weight
        self.habitat = habitat

    #Define the methods of the class
    def mammal(self):
        entry_size = input("How many feet long is the whale: ")
        entry_weight = input("Weight in pounds: ")
        if (entry_size == self.size and entry_weight == self.weight):
            print("Yo, that's a big {}".format(self.type))
        else:
            print("You're not a whale.")
#Outside of the class you would create an instance of the User class
new_type = Whale()
#Call the login method using the new object
new_type.mammal()

"""
Somehow with the above setup, I should be able to create a new object
in a single line of code:

    >>> New_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)
"""

class shark(Whale):
    weight = 5.00
    length = 'shorter'

class dolphin(Whale):
    blowhole = 'smaller'
    intelligence = 'higher'

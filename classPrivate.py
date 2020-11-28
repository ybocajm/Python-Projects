



class myOwnPrivateIdaho: #This is an object
    def __init__(self):
        self.__myOwnPrivateIdahoVar = 0

    def getPrivate(self):
        print(self.__myOwnPrivateIdahoVar)

    def setPrivate(self, private):
        self.__myOwnPrivateIdahoVar = private

obj = myOwnPrivateIdaho()
obj.getPrivate()
obj.setPrivate(2)
obj.getPrivate()
#print(obj._myOwnPrivateIdahoVar)

    
"""
This used to be class Game
#This is the basics of writing a class
These were variables for that class

    variable1 = "Hello"  #attributes and values to make a game object
    variable2 = "World!"
#next we need to instantiate - see Game() below

cept now I'm using encapsulation

This was all part of Game

#When Python sees this line, it goes right to it.
if __name__ == "__main__":
    #so if we were to call a function here (from above), it'll run it
    x = Game()
    print(x.variable1)
    print(x.variable2)
    #alternatively
    print("{} {}".format(x.variable1, x.variable2))
"""

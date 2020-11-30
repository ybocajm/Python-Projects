"""
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)
"""

class Privected:
    def __init__(self):
        self.me = 2
        self._me = 22
        self.__me = 222

p = Privected()
print(p.me,p._me,p._Privected__me)

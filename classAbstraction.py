

from abc import ABC, abstractmethod
class plane(ABC):
    def paySlip(self,amount):
        print("Amount:",amount)
# pass an argument, but dunno how/what kind (of data)
        @abstractmethod
        def payment(self, amount):
            pass

class DebitCardPayment(plane):
#implement payment function from parent (paySlip) class.
    def payment(self, amount):
        print("Amount  {} exceeded your $10000 limit ".format(amount))

obj = DebitCardPayment()
obj.paySlip("$50000")
obj.payment("$50000")
              

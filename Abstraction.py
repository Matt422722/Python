
#Importing ABC and abstractmethod from abc module
from abc import ABC, abstractmethod

#Abstract class 'Car' inherits from ABC
class Car(ABC):
    #method to print the purchase amount
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)

    #method must be implemented in any subclass of Car
    @abstractmethod
    def payment(self, amount):
        pass

#Child class 'DebitCardPayment' inherits from Car
class DebitCardPayment(Car):
    #Implementation of the abstract method 'payment'
    def payment(self, amount):
        print(f'Your purchase amount of {amount} exceeded your $100 limit.')

#Creating an object of DebitCardPayment
obj = DebitCardPayment()

#Calling the regular method from parent class
obj.paySlip("$400")

#Calling the abstract method from child class
obj.payment("$400")


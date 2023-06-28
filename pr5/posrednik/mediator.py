from abc import ABCMeta, abstractmethod
class IMediator(metaclass=ABCMeta):
    "The Mediator interface indicating all the methods to implement"
    @staticmethod
    @abstractmethod
    def colleague1_method():
        "A method to implement"
    @staticmethod
    @abstractmethod
    def colleague2_method():
        "A method to implement"
class Mediator(IMediator):
    "The Mediator Concrete Class"
    def __init__(self):
        self.colleague1 = Colleague1()
        self.colleague2 = Colleague2()
    def colleague1_method(self):
        return self.colleague1.colleague1_method()
    def colleague2_method(self):
        return self.colleague2.colleague2_method()
class Colleague1(IMediator):
    "This Colleague calls the other Colleague via the Mediator"
    def colleague1_method(self):
        return "Here is the Colleague1 specific data you asked for"
    def colleague2_method(self):
        "not implemented"
class Colleague2(IMediator):
    "This Colleague calls the other Colleague via the Mediator"
    def colleague1_method(self):
        "not implemented"
    def colleague2_method(self):
        return "Here is the Colleague2 specific data you asked for"
MEDIATOR = Mediator()

DATA = MEDIATOR.colleague2_method()
print(f"COLLEAGUE1 <--> {DATA}")

DATA = MEDIATOR.colleague1_method()
print(f"COLLEAGUE2 <--> {DATA}")
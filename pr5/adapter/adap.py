from abc import ABCMeta, abstractmethod
class IA(metaclass=ABCMeta):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def method_a():
        "An abstract method A"
class ClassA(IA):
    "A Sample Class the implements IA"
    def method_a(self):
        print("method A")
class IB(metaclass=ABCMeta):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def method_b():
        "An abstract method B"
class ClassB(IB):
    "A Sample Class the implements IB"
    def method_b(self):
        print("method B")
class ClassBAdapter(IA):
    "ClassB does not have a method_a, so we can create an adapter"
    def __init__(self):
        self.class_b = ClassB()
    def method_a(self):
        "calls the class b method_b instead"
        self.class_b.method_b()

ITEMS = [ClassA(), ClassB()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()

ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    item.method_a()
# Инверсия управления

your_name.py
```
config = {}

def your_name():
    output_function = config["OUTPUT_FUNCTION"]
    output_function("Your name, ")
```

your_name_people.py
```
people = []


def your_name_people():
    for person in people:
        print(f"Hello, {person}.")
```

main.py
```
import your_name

your_name.config["OUTPUT_FUNCTION"] = print

if __name__ == "__main__":
    your_name.your_name()
```

serzh.py
```
import your_name_people

your_name_people.people.append("Serzh")
```

## Диаграмма

```
@startuml Inversion_Of_Control
class YourName.your_name {
- config []
+ def your_name()
}
class YourName.your_name_people {
+ def your_name_people()
}
class YourName.main {
- config []
+ def your_name()
}
class YourName.serzh {
+ people.append()
}


YourName.your_name <|.. YourName.main
YourName.your_name_people <|.. YourName.main
YourName.serzh <|.. YourName.your_name
@enduml
```

![инверсия контроля](https://github.com/Smipos/TMP/blob/main/practices/practice_6/screens/Inversion_Of_Control.png)


# Заместитель (Proxy)

```
from abc import ABCMeta, abstractmethod
class ISubject(metaclass=ABCMeta):
    "An interface implemented by both the Proxy and Real Subject"
    @staticmethod
    @abstractmethod
    def request():
        "A method to implement"
class RealSubject(ISubject):
    "The actual real object that the proxy is representing"
    def __init__(self):
        self.enormous_data = [1, 2, 3]
    def request(self):
        return self.enormous_data
class Proxy(ISubject):
    def __init__(self):
        self.enormous_data = []
        self.real_subject = RealSubject()
    def request(self):
        if self.enormous_data == []:
            print("pulling data from RealSubject")
            self.enormous_data = self.real_subject.request()
            return self.enormous_data
        print("pulling data from Proxy cache")
        return self.enormous_data
    
SUBJECT = Proxy()

print(id(SUBJECT))
print(SUBJECT.request())
print(SUBJECT.request())
```

## Диаграмма
![Proxy](https://github.com/Smipos/TMP/blob/main/practices/practice_6/screens/proxy.png)

# Компоновщик (Composite)

```
from abc import ABCMeta, abstractmethod
class IComponent(metaclass=ABCMeta):
    reference_to_parent = None
    @staticmethod
    @abstractmethod
    def method():
        "A method each Leaf and composite container should implement"
    @staticmethod
    @abstractmethod
    def detach():
        "Called before a leaf is attached to a composite"
class Leaf(IComponent):
    "A Leaf can be added to a composite, but not a leaf"
    def method(self):
        parent_id = (id(self.reference_to_parent)
                     if self.reference_to_parent is not None else None)
        print(
            f"<Leaf>\t\tid:{id(self)}\tParent:\t{parent_id}"
        )
    def detach(self):
        "Detaching this leaf from its parent composite"
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
class Composite(IComponent):
    "A composite can contain leaves and composites"
    def __init__(self):
        self.components = []
    def method(self):
        parent_id = (id(self.reference_to_parent)
                     if self.reference_to_parent is not None else None)
        print(
            f"<Composite>\tid:{id(self)}\tParent:\t{parent_id}\t"
            f"Components:{len(self.components)}")
        for component in self.components:
            component.method()
    def attach(self, component):
        component.detach()
        component.reference_to_parent = self
        self.components.append(component)
    def delete(self, component):
        "Removes leaf/composite from this composite self.components"
        self.components.remove(component)
    def detach(self):
        "Detaching this composite from its parent composite"
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None

LEAF_A = Leaf()
LEAF_B = Leaf()
COMPOSITE_1 = Composite()
COMPOSITE_2 = Composite()
print(f"LEAF_A\t\tid:{id(LEAF_A)}")
print(f"LEAF_B\t\tid:{id(LEAF_B)}")
print(f"COMPOSITE_1\tid:{id(COMPOSITE_1)}")
print(f"COMPOSITE_2\tid:{id(COMPOSITE_2)}")
COMPOSITE_1.attach(LEAF_A)
COMPOSITE_2.attach(LEAF_A)
COMPOSITE_2.attach(COMPOSITE_1)
print()
LEAF_B.method()  
COMPOSITE_2.method() 
```

## Диаграмма

![Composite](https://github.com/Smipos/TMP/blob/main/practices/practice_6/screens/composite.png)

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
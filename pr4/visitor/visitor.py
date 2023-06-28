class Studying_In_Institute:
 
    def accept(self, visitor):
        visitor.visit(self)
 
    def teaching(self, visitor):
        print(self, "Taught by ", visitor)
 
    def studying(self, visitor):
        print(self, "studied by ", visitor)
 
 
    def __str__(self):
        return self.__class__.__name__
 
class SDE(Studying_In_Institute): pass
 
class STL(Studying_In_Institute): pass
 
class DSA(Studying_In_Institute): pass
 
class Visitor:
 
    def __str__(self):
        return self.__class__.__name__
 
class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)
 
 
class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)
 
sde = SDE()
stl = STL()
dsa = DSA()
 
instructor = Instructor()
student = Student()
 
sde.accept(instructor)
sde.accept(student)
 
stl.accept(instructor)
stl.accept(student)
 
dsa.accept(instructor)
dsa.accept(student)
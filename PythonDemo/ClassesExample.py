"""
class Student:
    x=10
    y=20
a=Student()
print(a.x)
print(a.y)

obj1=Student()
print(obj1.x)

obj2=Student()
print(obj1.y)



class Student:

    def __init__(self, firstName, lastName, stdID):
        self.firstName=firstName
        self.lastName=lastName
        self.stdID=stdID

obj=Student("Amol", "Chavan", 101)
obj1=Student("rahul", "pande",102)

print(obj.firstName)
print(obj.lastName)
print(obj.stdID)
print(obj1.firstName)
print(obj1.lastName)
print(obj1.stdID)

"""

class Student:

    def __init__(self, firstName, lastName, stdID):
        self.firstName=firstName
        self.lastName=lastName
        self.stdID=stdID

    def display(self):
        print(self.firstName, " ", self.lastName, "  ", self.stdID)


obj=Student("Amol", "Chavan", 101)
obj1=Student("rahul", "pande",102)
obj2=Student("mangesh", "Nikam",103)

obj.display()
obj1.display()
obj2.display()
obj2.display()
obj2.display()

obj2.stdID=110
obj2.display()


class Animal:
    pass


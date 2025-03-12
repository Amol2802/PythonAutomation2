"""
# Inheritance
class Person:

    def __init__(self,car,bike):

        self.carName=car
        self.bikeName=bike

    def show(self):
        print(self.carName,"   ", self.bikeName)


class Child(Person):
    pass

obj=Child("Audi","R15")
obj1=Person("VW","Honda")
obj2=Person("Tata","TVS")

obj.show()
obj1.show()
obj2.show()


class Person:

    def __init__(self,car,bike):

        self.carName=car
        self.bikeName=bike

    def show(self):
        print(self.carName,"   ", self.bikeName)

class Child(Person):

    def __init__(self, car, bike):
        super().__init__(car, bike)
        Person.show(self)

obj=Child("Hundai23","Suzuki346")

obj.show()

"""

class Person:

    def __init__(self,car,bike, modelYear):

        self.carName=car
        self.bikeName=bike

        self.modelYear = modelYear
    def show(self):
        print("This is parrent class show method",self.carName,"   ", self.bikeName, self.modelYear)

class Child(Person):

    def __init__(self, car, bike,modelYear ):
        super().__init__(car, bike,modelYear)
        self.modelYear=modelYear

    def show(self):
        print("This is child class show method",self.carName, "   ", self.bikeName, self.modelYear)

a=Child("Audi","FZ", 2018)
#a.show()
#print(a.modelYear)

b=Person("VW","Unicon",'2022')
b.show()


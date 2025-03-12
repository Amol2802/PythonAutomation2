"""
# operator overloading
a=10
b=20
print(a+b)
name="Amol"
lastName="Chavan"
print(name + lastName)
c="20"
d="50"
print(c+d)

class A:
    def sum(self, a, b):
        self.a=a
        self.b=b
        c = a +b
        print(c)

    def sum(self, a, b, c):
        self.a=a
        self.b=b
        self.c = c
        d = a +b+c
        print(d)


a= A()
a.sum(40,70)
a.sum(20,40, 40)
a.sum(30,40,60)


def add(self,a, b):
    print(a+b)

def add(self,a, b, name:
    print(a+b+c)

add(20,40, "Amol")


# Method overriding and multilevel inheritance
class A:
    def show(self):
        print("I am show method of class A")

    def show1(self):
        print("I am show method of class XYZ")

class B(A):

     def show(self):
         super().show1()
         A.show(self)

         print("I am show method of class B")

class C(B):

    def show(self):

        super().show()
        print("I am show method of class c")

c=C()
#c.show()
"""
#Multipple Inheritance
class A:
    def show(self, a,b):
        result=a+b
        print("I am show method of class A", result)

class B:

    def show1(self, c,d,z):
        result = c + d +z
        print("I am show method of class B", result)

class C(A,B):
    def show(self,a,b):
        result = a + b +c
        print("I am show method of class c", result)

    def show1(self, c,d,z):
        result = c + d +z
        print("I am show method of class B", result)

c=C()
c.show1(20,70,20)

a=A()
a.show(100,400)

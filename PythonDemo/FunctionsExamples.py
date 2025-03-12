"""
# Functions
def addition():
    a=10
    b=20
    c= a+b
    print(c)

addition()

def substraction():
    a=50
    b=10
    c= a-b
    print(c)

substraction()


def firstName(fname):
    print("My name is " ,fname)

firstName("Amol")
firstName("Rahul")
firstName("Nilesh")

def add(a, b):
    print(a+b)

add(10,40,)

add(60,90)


def eating(*fruits):
    print("I am eating ", fruits)
    print("I am eating ", fruits[2])

eating("Apple", "mango", "Orange")

def eating(**Name):
  #  print("My name is ", Name["fname"])
   # print("My lastname is ", Name["lName"])
   # print("My bom no is ", Name["mobNo"])

    print("My deatils is ", Name["fname"],Name["lName"], Name["mobNo"])

eating(fname="Amol", lName="Chavan", mobNo="873664896")


def firstName(fname="Rahul"):
    print("My name is " ,fname)

#firstName("Amol")
#firstName("nilesh")
firstName()

def show(country):
    for a in country:
        print(a)

c = ["India", "Us", "UK", "Canada"]

show(c)
show(["shri", "AUS", "GERMANY", "France"])

def m():
    pass
"""
def multi(a , b):
    print("Ia m in multplication")

    return a * b

f=multi(30,20)
#print(f)

def dubMul(g, r):
    return f * r

print(dubMul(f, 20))
print(dubMul(f, 10))
print(dubMul(f, 50))






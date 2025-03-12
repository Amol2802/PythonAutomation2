
import numpy
"""
b=20   # Global variable

def m():
     a=10  # local variable
     print(a)
     print(b)

m()
print(b)


def show():
    global t
    t="Amol"
    print(t)

show()
print(t)


t="Rahul"

def show():
    global t
    t="Amol"
    print(t)


show()
print(t)
"""
t="Rahul"    # global variable

def show1(a):
    global t    # global variable
    t=a
    print(t)

    f=20        # local variable
    print(f)


show1("Nilesh")
print(t)
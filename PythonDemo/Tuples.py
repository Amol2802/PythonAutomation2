"""
t=("Apple", "Mango", "Banana", "Apple")

#print(type(t))
#print(t)

#t[1]="Orange" # C.E
#print(t)

# Accessing the tuples values
t=("Apple", "Mango", "Banana", "Apple")
#print(t[2])
#print(t[0:3])
#print(t[:])

if "Banana764" in t:
    print("Banana is present ")
else:
    print("Banana is not present ")

# Updation
t=("Apple", "Mango", "Banana", "Apple")
print(t)
list1= list(t)
print(list1)
list1.insert(2, "Orange")
list1.append("Graphs")
print("After change ", list1)
list1.remove("Graphs")
print("After Remove ", list1)
t=tuple(list1)
print("After conversion in to tuple", t)
"""
# Loops
"""
t=("Apple", "Mango", "Banana", "Apple")

for a in t:
    if "Mango" == a:
      print(a, " is present")
    else:
        print(a, " is not present")

t=(10, 40, 60, 40, 10, "Amol", "rahul")
count=len(t)
print(count)

for i in range(count):
    print(t[i])

# join
t1=(10, 40, 60, 40, 10)
t2= ("Amol", "Rahul")
print(t1)
print(t2)

t3= t2 + t1
print(t3)

t4= t1*3
print(t4)

"""
# packing
t= ("Amol", "Rahul", "Nikhil")
#print(t)

#Unpacking
t1= ("Amol", "Rahul", "Nikhil")

(st1, st2, st3) =t1

print(st1)
print(st2)
print(st3)

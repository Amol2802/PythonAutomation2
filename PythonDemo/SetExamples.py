"""
s={"Apple","Mango", "Orange","Apple"}
print(s)
#print(type(s))

# In set True consider as 1 and False consider as 0
s={"Apple","Mango", True,False, "Orange", 2, 1, 0}
print(s)

# length
s={"Apple","Mango", "Orange","Apple", True, 1}
print(len(s))

s1 = set(("Apple","Mango", "Orange"))
print(s1)

# Loops
s={"Apple","Mango", "Orange"}

for a in s:

    if "Mango" == a:
        print(a," is present")
    else:
        print(a, "Not present")

s={"Apple","Mango", "Orange"}

print("Graphs" not in s)


# add the items into set
s={"Apple","Mango", "Orange"}
print("Before Add :-", s , "Length of set", len(s))
s.add("Graphs")
print("After Add :-", s, "Length of set", len(s))


# add the multiplr items into set
s={"Apple","Mango", "Orange"}
s1={1, 4, 8 ,10}
s.update(s1)
print(s)

# add the list items into set
s={"Apple","Mango", "Orange"}
s1=[1, 4, 8 ,10]
s.update(s1)
print(s)

# Remove
s={"Apple","Mango", "Orange", "Apple"}

#s.remove("Mango")
#s.remove("Graphs")  #Error
print("Before Remove :- ",s)
s.discard("Graphs")
print("After Remove :- ",s)
s={"Graphs","Apple","Mango", "Orange",}
print("Before Remove :- ",s)
s.pop()
print("After Remove :- ",s)


# clear and del
s={"Apple","Mango", "Orange", "Apple"}
print(s)
#s.clear()
del s

# joint
s={"Apple","Mango", "Orange"}
s1={1, 4, 8 ,10}
s2={11, 14, 81,10}
#s.update(s1)
s3=s.union(s1, s2)
print(s3)


s={"Apple","Mango", "Orange"}
s1={1,2,3}

s3= s1 | s
print(s3)
"""
s={"Apple","Mango", "Orange"}
s1={1, 4, 8 ,10}
s2={11, 14, 81,10}
#s.update(s1)
s3=s.union(s1, s2)
print(s3)

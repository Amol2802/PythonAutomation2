"""
list = ["Apple", "Mango", "Graphs", "Banana", "Mango"]
print(list)
list[2]="Apple"
print(list)

# to check the length of the list
list1 = ["Apple", "Mango", "Graphs", "Banana", 4]
print(type(list1))
print(list1)
print(len(list1))

# list as a constuctore
l=list((1, 4, 5, 8))
print(l)

# Negative indexing
list1 = ["Apple", "Mango", "Graphs", "Banana", 4]

print(list1[-4])
print(list1[1])

# Indexing range
list1 = ["Apple", "Mango", "Graphs", "Banana", 4]
#print(list1[2:5])
print(list1[:])
print(list1[0:])
print(list1[:5])
print(list1[-5:])
print(list1[1:-2])

print(list1[1])
print(list1[3])

# items check
if "Mango" in list1:
    print("yes mango is preasnt")
else:
    print("mango not present")

if "Banana" in list1:
    print("yes Banana is preasnt")
else:
    print("Banana not present")

# copy the list
list1 = ["Apple", "Mango", "Graphs", "Banana", 4]
#list2=list1
list2=list1.copy()
print(list2)
print(list1)


# insert the elements or items
list1 = ["Apple", "Mango", "Graphs", "Banana", 4]

list1[2]=80
print(list1)

list1.insert(2, 56)
print(list1)

# Append the items
list1 = ["Apple", "Mango", "Graphs", "Banana", 4]
list1.append("Orange")
print(list1)

# Extend the list
list1=[1,2,3]
list2=[4,5,6]

#list1.extend(list2)
print(list1)
list2.extend(list1)
print(list2)


# REmoving elements
list1 = ["Apple", "Mango", "Graphs", "Banana"]
print(list1)
#list1.remove(2)
#list1.pop(3)
#list1.pop()
#del list1    # deleting the list
#del list1[0]
#list1.clear()   # removing the all list items
print(list1)
#print(list1)


# Loops in List or iterating the list values
list1 = ["Apple", "Mango", "Graphs", "Banana","Applegtdg","bshtdvdfg"]

#for a in list1:
#   print(a)

#for x in range(len(list1)):
 #   print(list1[x])

list1 = ["Apple", "Mango", "Graphs", "Banana","Applegtdg","bshtdvdfg"]

i = 0
while i < len(list1):
     print(list1[i])
     i = i + 1

# sorting the list items
list1 = ["Apple","Mango","apple","Graphs", "Banana", "Apple"]
print(list1)
list1.sort()
print("asceding",list1)
list1.sort(reverse=True)
print("descending",list1)

list2 = [5,3,1,89,33,0,67,34,56,80]
print(list2)
list2.sort()
print("asceding",list2)
list2.sort(reverse=True)
print("descending",list2)

# Copy the list into new list
list1 = ["Apple","Mango","apple","Graphs", "Banana", "Apple"]
#newlist = list1.copy()
#newlist=list(list1)
#newlist = list1[:]
#print(newlist)
"""
# joining the 2 lists
list1 = ["Apple","Mango","apple","Graphs", "Banana", "Apple"]
list2 = [4,3,9,2,0]
#list3= list1 + list2
#list1.extend(list2)

for a in list2:
    list1.append(a)
print(list1)


"""
i=0
while i <= 10 :
    print(i)

    if i == 7:
        break
    i +=1

i=0
while i < 10 :

    i += 1
    if i == 6:
        continue
    print(i)

i=10
while i >= 0 :
    print(i)
    i -=1
"""

# for loop
"""
for i in range(0,101,2):
    print(i)


for a in range(8):

    if a == 4:
        break
    print(a)

for a in range(8):
    if a == 5:
        continue
    print(a)

# iterating list values
li=[10,20,30,67, 89, 834, 429,300]
print(li)

for a in li:
    print(a)

    if a==89:
        break


# slplit string into characters
a= "amol"
print(a)

for ch in a:
    print(ch)


l1=[10,20,30,40]
l2=[1,2,3,4]

for a in l1:
    for b in l2:
        print(a,b)

"""
for i in range (1,10):
    for j in range(i):
        print("*", end= " ")

    print()


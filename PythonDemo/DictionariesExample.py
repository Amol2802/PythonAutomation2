
"""
d={
   "year" : 2022,
    "brand" : "Audi",
    "model" : "Q8",
}
print(d)
d["year"]=2024
print(d)
print(type(d))



d1= dict (
    year = 2022,
    brand = "Audi",
    model = "Q8",
)
print(d1)
print(type(d1))

# accessing the items
d1= dict (
    year = 2022,
    brand = "Audi",
    model = "Q8",
)
print(d1)
print(d1["year"])

modelValue=d1.get("model")
print(modelValue)

keys1=d1.keys()
print(keys1)

print(d1.values())

print(d1.items())

# Updation
d={
   "year" : 2022,
    "brand" : "Audi",
    "model" : "Q8",
}
#print(d)
#d["year"]=2025
#print(d)

print(d)
d.update({"model" :"Q3",  "brand" : "Tata",})
print(d)

# Add Items
d={
   "year" : 2022,
    "brand" : "Audi",
    "model" : "Q8",
}
print(d)
#d["fuel"]="Petrol"
d.update({"color":"Black", "fuel":"Petrol"})
print(d)


# Remove Items
d={
   "year" : 2022,
"fuel":"Petrol",
"color":"Black",
    "model" : "Q8",
    "brand" : "Audi",
}
print(d)
#d.pop("brand")
#d.popitem()
#del d["model"]
#del d
d.clear()
print(d)

# loops
d={
   "year" : 2022,
   "fuel":"Petrol",
   "color":"Black",
    "model" : "Q8",
    "brand" : "Audi",
}

# for loops kyes
#for a in d:
#    print(a)

# for loops vaues
#for a in d:
 #   print(d[a])

for a, b in d.items():
    print(a," = ", b)
"""

# copy the dict

#duplict_d=d.copy()
#dupl=dict(d)
#print(dupl)

#dup=d
#print(dup)

# neseted Dict
d={
    "Audi":{
   "year" : 2022,
   "fuel":"Petrol",
   "color":"Black",
    "model" : "Q8",
    },

"tata": {
   "year" : 2023,
   "fuel":"Diesel",
   "color":"Black",
    "model" : "nano",

    },
"Vw":{
   "year" : 2023,
   "fuel":"Diesel",
   "color":"red",
    "model" : "polo",

    }
}

print(d)

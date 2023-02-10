#LUIT session notes

import random

var = {}

print(var)
print(type(var))

var2 = {"fruit": "apple", "juice":"cranberry", "food":"spaghetti"}

print(var2)

print(var2["juice"])

for k, v in var2.items():
    print(k, v)
 
var2["drank"] = "petron"
print(var2)

var2["fruit"] = "grape"
print(var2)

var2["fruit"] = ["apple", "grape"]
print(var2)
print(var2["fruit"][0])

print(list(var2.keys()))
print(list(var2.values()))

print(dir(var2))

dict_of_dict = {j:{i:random.randint(0,10) for i in range(5)} for j in range(5)}
print(dict_of_dict)

for k, v in dict_of_dict.items():
    print(k, v)
    
print(dict_of_dict[3][2])

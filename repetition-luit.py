# LUIT session notes

import random

#%%
# FOR

for i in range(5):
    print("hi")

numbers = list(range(0,5))

print(numbers)

for number in numbers:
    print(number)
    
#%%
# WHILE

number = random.randint(0,100)
counter = 0

while(number != 55):
    number = random.randint(0,100)
    counter = counter + 1 # counter += 1
    
print(counter, number)

# WHILE # BREAK

number = random.randint(0,10000)
counter = 0

while(number != 55):
    if(counter != 10000):
        number = random.randint(0,10000)
        counter = counter + 1 # counter += 1
    else:
        break
    
print(counter, number)

#%%
# For -> while # DO NOT DO THIS

number = random.randint(0,10000)

for i in range(10000):
    if(number != 55):
        number = random.randint(0,10000)
    else:
        break

print(i, number)

#%%
# while -> for # DO NOT DO THIS

numbers = list(range(0,5))

counter = 0
while(counter < len(numbers)):
    print(numbers[counter])
    counter = counter + 1

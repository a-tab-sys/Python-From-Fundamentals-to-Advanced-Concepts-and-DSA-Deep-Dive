# 29 random numbers using random module.
    #need to import random library for this: import random

x=random.randint(1,6)       #rando int within a specified range
y = random.random()         #random floating number btween 0 and 1

myList = {'rock', 'paper', 'scissors'}      #use with a list or other collection
z=random.choice(myList)

cards=[1,2,3,4,5,5,6,7,8,9,10,"j","q","k","a"]
random.shuffle(cards)

print(x)
print(z)
print(cards)
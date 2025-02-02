# 51 Walrus Operator :=    - assigns values to variables as part of a larger expression

happy = True
print(happy)

print(happy := True)    #does the same thing as above

foods=list()
while True:
    food=input("what food would you like?: ")
    if food=="quit":
        break
    foods.append(food)

    #does what the above program does but uses walrus operator and less lines
foods=list()
while food := input ("What food do you like?: ") != "quit":
    foods.append(food)
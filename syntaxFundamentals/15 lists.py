#15 Lists - used to store multiple items in a single variable
food = ["pizza", "hamburger", "spaghetti"]

print(food)
print(food[2])

    #Change an element in list
food[0]='sushi'
print(food[0])

    #print all items in list
for x in food:
    print(x)

    #different functions you can use. o access them type <list name>.
    #append means we added ice cream to end of our list
food.append("ice cream")

    #print all items in list
for x in food:
    print(x)

    #remove lets us remove a cetain element in list
food.remove("sushi")

    #print all items in list
for x in food:
    print(x)

    #pop removes the last element
food.pop()

    #print all items in list
for x in food:
    print(x)

    #insert lets you add an element to a certain index
food.insert(0, "cake")

    #sorts a list alphabetically
food.sort()

    #clears the entire list, removes all elements
food.clear()

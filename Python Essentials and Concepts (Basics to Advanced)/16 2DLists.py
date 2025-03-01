#16 2D Lists - a list of lists
drinks=["coffee", "soda", "tea"]
dinner=["pizza", "hamburger", "hotdog"]
dessert=["cake", "icecream"]

food=[drinks, dinner, dessert]      #combine all lists
print(food)     #access all lists
print(food[0])     #access just one list by ading an index, index 0 is the first list, drinks
print(food[0][2])      #access a certain element within a certain list, first list, third element in that list

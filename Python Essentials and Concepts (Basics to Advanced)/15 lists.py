#15 Lists - used to store multiple items in a single variable
food = ["pizza", "hamburger", "spaghetti"]

print(food)
print(food[2])

    #Change an element in list
food[0]='sushi'
print(food[0])

#refer to last element in list
print("last element: "+food[-1])

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

my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # Output: 5


# To print the index of elements in a Python list, you can use the enumerate() function. Here's an example:
my_list = ['apple', 'banana', 'cherry']

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

nums=[2,3,4,5,6]
for i, x in enumerate(nums):
    print(f"Index: {i}, Value: {x}")


print(sum(nums))
print(max(nums))
print(nums.index(4))
nums.remove(4)
print(nums)

for x in nums:
    print(x)

# The .extend() method in Python is used to add 
# multiple elements from one iterable (like a list, tuple, etc.)
# to the end of another list. It extends the list in place, 
# meaning it modifies the original list directly rather than 
# creating a new one.

list1=[1]
list1.extend(nums)
print(list1)
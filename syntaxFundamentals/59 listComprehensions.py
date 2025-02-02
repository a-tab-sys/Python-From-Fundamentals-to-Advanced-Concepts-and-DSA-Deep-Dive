# 59 List Comprehensions-way to create a new list with less syntax
                        #can also mimic certain lambda functions (like the map and filter function), easier to read
                        #list = [expression for item in iterable]       //if you have no conditional
                        #list = [expression for item in iterable if conditional]           //if you have if    
                        #list = [expression if/else for item in iterable]       //if you have if/else

squares = []
for i in range(1, 11):
    squares.append(i*i)
print(squares)
    #this does same thing as above, less syntax
squares = [i*i for i in range(1, 11)]   #i*i is expression, for i is the iem, range(1, 11) is the iterable
print(squares)

#another example
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

#passed_students=list(filter(lambda x: x>= 60, students))    #uses filter function

passed_students = [i for i in students if i>=60]     #uses list comprehension. expression: i, item: i, iterable: students
passed_students = [i if i>=60 else "FAILED" for i in students]     #if you need if/else statement its added after the expression. if you only need if statement its added after the iterable


print(passed_students)
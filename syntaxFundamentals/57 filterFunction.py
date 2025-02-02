# 57 filter function - lets you search for something that meets a certian criteria
# filter() = creates a collection of elements from an iterable for which a function returns true
# filter (funtion, iterable)

friends=[("Rachel", 19),
         ("Monica", 18),
         ("Phoebe", 17),
         ("Joey", 16),
         ("Chandler", 21),
         ("Ross", 20)]

#what if i wanted to create a seperate list for all the friends that are 18 or older

age = lambda data: data[1] >=18 
#filter our iterable by the function of age

#filter(age, friends)    #filter function returns a filter object, you can cast it to another iterable
drinking_buddies=list(filter(age, friends))

for i in drinking_buddies:
    print(i)
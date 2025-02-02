#58 Reduce function
    # reduce() - apply a function to an iterable and reduce it to a sinle cumulative value
    #performs function on first 2 elements and repeats process until 1 value remains
    #import functools
    # reduce (function, iterable)

letters=["H","E","L","L","O"]        #list
    #i want to reduce all these elements into a single value
    #can use reduce funcion or a for loop
word=functools.reduce(lambda x, y:x+y, letters)     #saving to variable named word. lambda is the function, letters is the iterable

print (word)

# the reduce function applies out lambda function to the first 2 elements in the iterable
#["H","E","L","L","O"] 
#["HE","L","L","O"] 
#["HEL","L","O"] 
#["HELL","O"] 
#["HELLO"] 

#another example - calculating factorial
factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y, :x*y, factorial)
print(result)
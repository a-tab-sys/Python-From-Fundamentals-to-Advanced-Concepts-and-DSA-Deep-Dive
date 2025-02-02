# 28 string format, str.format() - optional method. gives more control when displaying output.

animal = "cow"
item = "moon"

print("The " + animal+ " jumped over the "+ item)
    #we can write the above line better
print("The {} jumped over the {}".format("cow", "moon"))        #useing string
print("The {} jumped over the {}".format(animal, item))         #using variables
print("The {1} jumped over the {0}".format(animal, item))       #use positional argument to pick which argument is placed where
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))       #keyword arguments, for this you didnt need the initial initializations

text="The {} jumped over the {}"        #text is a variable. {} is a format field
print(text.format(animal, item))
    
    #add some padding to a string when we display it
name = "Bro"
print("Hello, my name is {}". format(name))      #allocating 10 spaces of space
print("Hello, my name is {:10}. Nice to meet you". format(name))
print("Hello, my name is {:<10}. Nice to meet you". format(name))    #left align
print("Hello, my name is {:>10}. Nice to meet you". format(name))    #right align
print("Hello, my name is {:^10}. Nice to meet you". format(name))    #center the value
    #to add positional or keyword argument to the format field, preceed the colon
#print("Hello, my name is {name:10}. Nice to meet you". format(name))

    #formatting numbers
number = 3.14159
print("The number pi is {}".format(number))
print("The number pi is {:.2f}".format(number)) #display only first 2 digit after decimal. f for floating point number. this will also round your number
number1=1000
print("The number pi is {:,}".format(number1))  #adds comma to thousants places
print("The number pi is {:b}".format(number1))  #display binary representation. can also do with hexidecimal, octal, etc
print("The number pi is {:E}".format(number1))   #display scientific notation

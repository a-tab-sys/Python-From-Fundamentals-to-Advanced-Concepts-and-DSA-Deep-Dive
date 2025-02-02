# 27 kwargs - parameter that will pack all arguments into a diction#ary
            # useful so that a function can accept varying amount of keyword arguments

def hello (first, last):
    print("Hello " + first + " "+ "last")
#hello(first="Bro", middle="Dude", last="Code")     #cant to this bc we got an unexpected keyword argument


    #to allow varying number of key board arguments, do as below
def hello (**kwargs):
    print("Hello " + kwargs['first'] + " "+ kwargs['last'])
hello(first="Bro", middle="Dude", last="Code")


    #to display someones full name based on how many keyword arguments they pass
def hello (**kwargs):           #does not have to be called kwargs
    print("Hello", end=" ")     #instead of going to new line it will create a space
    for key, value in kwargs.items():   #iterate through each key value pair in dictionary and print each value
        print(value, end=" ")
hello(first="Bro", middle="Dude", last="Code")
hello(title="Mr.", first="Bro", middle="Dude", last="Code")

    #QUESTION: but dictionaries are unordered, so will it ever display in comletly random order?????????????????????????????
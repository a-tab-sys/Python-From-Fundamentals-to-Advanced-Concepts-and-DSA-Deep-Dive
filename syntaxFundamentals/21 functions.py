#21 Functions - a block of code which is executed only when it is called
    #defining function
def hello():
    print('hello!')

def hello1(name):
    #pass    #if you dont know what it should do yet
    print('hello '+name)
    print('have a nice day')

hello()     #executes block of code
hello1("Bro") #sending function some information, hello is recieving a string value, one argument. this parameter has to be accounted for in function definition.

my_name="broCode"
hello1(my_name)

def hello2(first_name, last_name, age):      #accept 3 arguments
    print("hello " + first_name +" "+ last_name +' you are '+str(age))      #cast as string for the integer
hello2("john", "schneedle", 21)
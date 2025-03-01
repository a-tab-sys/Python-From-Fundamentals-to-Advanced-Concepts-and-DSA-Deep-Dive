import math
import time
import random
import os
import shutil
import functools
import threading
from abc import ABC, abstractmethod
from multiprocessing import Process, cpu_count
"""
#Printing a message
print('hello world')
print("hello world")

#Variables (String, Int, Float, boolean)
StringEx="text"
StringEx2='text'
IntEx=3
BooleanEx=False

#Concatenate statements
print("this is  "+StringEx)

#Check variable datatype on console
print(type(StringEx))

##Combine variables of same data type
    #string Ex
first_name = "Bro"
last_name= 'Code'
full_name= first_name+ " " +last_name
print("Hello" + full_name)
    #int Ex
age=21
#age=age+1
age+=1
print(age)
print(type(age))
##print ("your age is: " + age) : this will not work, cannot contatenate 2 diff data types, need type casting

#Type casting
print ("your age is: " + str(age))

#Float data type - stores decimal numbers
height = 250.5
print(height)
print(type(height))
print("your height is: "+str(height) +"cm")

#Boolean data type - true or false
human=False
print(human)
print(type(human))
print("are you a human: "+str(human))

"""
"""

#03 Multiple Assignment - allows us to assign many vaiable at once with one line of code
name="bro"
age=4
atttractive=True

name, age, attractive="bro", 21, True
spongebob = patrick = sandy = squidward = 30

"""
"""

#04 Useful string methods
name="Bro Code"

    #prints length of string - would output 8
print(len(name))

    #finds where the first index of a certain character is, starts counting at 0...1...2
print(name.find("o"))

    #capitalize only the first letter of your entire string
print(name.capitalize())

    #makes your string all uppercase
print(name.upper())

    #makes your string all lowercase
print(name.lower())

    #returns true or false depending on whether the string is entirely composed of digits - would output false
print(name.isdigit())

    ##returns true or false depending on whether the string is entirely composed of alphabetical characters - would output false because we have a space in it
print(name.isalpha())

    ##Counts how many character are within our string - returns 2
print(name.count("o"))

    ##replaces a certain character, accepts 2 arguments("what to replace", "what to replae with")
print(name.replace("o", "a"))

    #display a string multiple times
print(name*3)

"""
"""

#05 Type Casting - convert a data type of a value to another data type
x=1         #int
y=2.0       #float
z="3"       #str

print(x)
print(y)
print(z)

print(int(y))
print(float(z))

print(int(z)*3)
print(z*3)

"""
"""

#06 Accepting user input
input("wht is your name? ")

    #save to variable
name1=input("wht is your name? ")
print("hello "+ name1)

    #default input is string, you need to type cast to diff data type to do calculations on inputted data
age=input("How old are you?: ")
#age= age + 1                                   wont work because you are doing calc on a string and int 
print("your age is: "+age)
    
    #instead we can use type casting when accepting input
age2 = int(input("How old are you?: "))         #use float instead to accept decimal inputs
age2=age2 + 1
#print("your age is"+age2)                      wont work bc you are concatenating a string and int
print("your age is: "+str(age2))

"""
"""

#07 Math Functions
    #for starters, use import math at start of program to import the math module. if you type math. you will see a list of functions
pi=-3.14
    #round a number to nearest int
print(round(pi))
    #round number up
print(math.ceil(pi))
    #round number down
print(math.floor(pi))
    #get the abs value
print(abs(pi))
    #raise base number to a power, 2 arguments: base, exponent
print(pow(pi, 2))
    #square root funct
#print(math.sqrt(pi))       wont work bc you are sqare rooting a negative
print(math.sqrt(420))
    #will find the largest or lowest of a varying amout of values
a=1
b=2
c=3
print(max(a, b, c))
print(min(a, b, c))

"""
"""

#08 String Slicing - create  substring by extracting elements from another spring
#   indexing[] or slice[]
#   [start:stop:step]       indexing starts at 0. start index num is inclusive, end index number is exclusive, default for step is 1, that just normal writing

name='Bro Code'
print(name[0])

first_name=name[:3]         #[0:3]      , leave start index empty=default is index 0

last_name=name[4:]          #[4:8]      , leave stop index empty=default is end of string

funky_name=name[::2]        #[0:8:2]

    #reverse string in python
reversed_name=name[::-1]    #[0,8,-1]   , because step of 1 is just regular writing, so -1 is reverse writing

print(first_name)
print(last_name)
print(funky_name)

    #create a substring based on website name indexing (0...1...2...) (3...2...1)
website="http://google.com"
slice = slice(7, -4,)
print(website[slice])

"""
"""

#09 if statements
age=int(input("How old are you: "))

if age==100:
    print("you are a century old")
elif age>=18:
    print("you are an adult")
elif age<0:
    print("you have not been born")
else:
    print("you are a child")

"""
"""

#10 logical operators (and, or, not)
temp=int(input("What is the temprature outside?: "))

if not(temp>=0 and temp<=30):
    print("Stay in, bad temp")
elif not(temp<0 or temp>30):
    print("Go out, good temp")

"""
"""

#11 While Loops - will excecute code, as long as its condition is true
name=""
while len(name) ==0:            #while the length of the name is 0
    name = input("enter your name: ")
print("Hello "+name)

    #another way to write the above
name2=None
while not name:
    name=input("enter your name: ")
print("Hello "+name)

"""
"""

#12 For Loops - will execute a limited amount of times
for i in range(10):  #Excecutes 10 times
    print(i)         #shows 0-9

for index in range(10):
    print(index+1)    #shows 1-10

    #you can work index in a specific range
for index1 in range(50, 100):
    print(index1)           #shows 50-99.runs 50 times. first number is inclusive, second is exclusive

    #you can add a third number to this range to specify how much you want to count up or down by
for index2 in range(50, 100+1,2):   #shows 50-100 because of the +1, skips up by 2.
    print(index2)

for index3 in "Bro Code":
    print(index3)               #prints Bro Code   
  
    #For example below we will cound down and then say happy new year. need to import time module at start of program
for seconds in range(10, 0,-1):
    print(seconds)
    time.sleep (1)      #tells to sleep 1 sec between each iteration of for loop
print("happy new year")

"""
"""

#13 Nested loops - inner loop will finish all its iterations before finishing one iteration of outer loop

    #making  program that draws a rectangle of centain symbol - inner loop in charge of columns

rows=int(input("How many rows?: "))
columns=int(input("How many columns?: "))
symbol=input("enter a a symbol to use?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")       #once youve printed the collumn symbols, you dont want your cursor to move to next line so add this end="" to avoid that
    print()                         #this moves cursor to next line

"""
"""



"""#14 Loop control statements (break, continue, pass)
    #break = used to termainate loop entirely
    #continue = skips to next iteration of loop
    #pass = does nothing, acts as a placeholder

    
    #break statement - used to termainate loop entirely
    #program continually asks for name until one is entered, once one is entered it breaks
while True:
    name = input("Enter your name: ")
    if name != "":
        break
 
    #program removes dashed from phone numbers
    #continue statement - skips to next iteration of loop
phone_number = "123-456-7890"
for i in phone_number:
    if i=="-":
        continue
    print(i, end="")

     #pass = does nothing, acts as a placeholder
     #prints all numbers except 13
for i in range(1, 21):
    if i ==13:
        pass
    else:
        print(i)
"""

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

"""
"""

#16 2D Lists - a list of lists
drinks=["coffee", "soda", "tea"]
dinner=["pizza", "hamburger", "hotdog"]
dessert=["cake", "icecream"]

food=[drinks, dinner, dessert]      #combine all lists
print(food)     #access all lists
print(food[0])     #access just one list by ading an index, index 0 is the first list, drinks
print(food[0][2])      #access a certain element within a certain list, first list, third element in that list

"""
"""

#17 Tuples - similar to lists. collections which are ordered and unchangeable
#            used to group together related data

student = ("Bro", 21, "male")
print(student.count("Bro")) #shows how many times bro apperars in touple
print(student.index("male"))    #shows what index male is at

print(student)

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")

"""
"""

#18 Sets - collections which is unordered, unindexed.  No duplicate values allowed
utensils={"fork", "spoon", "knife"}
dishes={"bowl", "plate", "cup", "knife"}

seen = set()        #creates an empty set

for x in utensils:
    print(x)        #because its unindexed and unordered, when you print the items, it is in random order
#                    also faster processing because of this

    #see what happens when you add duplicate values
utensils1={"fork", "spoon", "knife", "knife", "knife"}
for x in utensils1:
    print(x)            #knife is only shown once

    #when you type <set name>. you will get list of funcions
    #adds element
utensils.add("napkins")
for x in utensils:
    print(x) 
    #removes element
utensils.remove("fork")
for x in utensils:
    print(x) 
    #clears set
utensils.clear()
for x in utensils:
    print(x) 

    #add one set to the other using update method
    #adds all elements in dishes set to utensils set
utensils.update(dishes)
for x in utensils:
    print(x)

    #join 2 sets to create an entirely new set
dinner_table=utensils.union(dishes)     #or vice versa

    #compare similarities nd differences between elements of different sets
    #prints what utensils has that dishes does not
print(utensils.difference(dishes)) #or vice versa
    #prints what utensils has in common with dishes
print(utensils.intersection(dishes))  

"""
"""

# 19 Dictionary - a changeable, unordeered collections of unique key: value pairs
#               - fast because they use hashing, allow us to access a value quickly
#               - (key: value)
capitals = {'USA' : 'Washington DC', 
            'India':'New Dehli', 
            'China': 'Beijing',
            'Russia' : 'Moscow'}
    
    #to print from dictionary using the key
    #if use a key that does not exist like Germany, you get error
    #use get method to avoid this
print(capitals['Russia'])
#print(capitals['Moscow'])  cant do this, you can only look up keys, moscow is a value

print(capitals.get('Germany')) #return None
print(capitals.keys())  #prints all the keys, not the values
print(capitals.values())    #prints all the values, not the keys

capitals.update({'Germany': 'Berlin'})      #add key, value pair to ditionary
capitals.update({'USA':'Las Vegas'})        #updates existing key with new value
capitals.pop('China')       #remove pair associated with china
capitals.clear()     #clears entire dictionary

print(capitals.items())     #displays everything in dictionary (keys and values)

for key,value in capitals.items():      #displays everything in dictionary (keys and values)
    print(key, value)

"""
"""

#20 Indexing
#   index operator [] = gives access to a sequences element (string, list, tuples)

name='bro code!'
if (name[0].islower()):     #checks is names first letter is caitalized, if it is not it capitalizes it
    name=name.capitalize()
print(name)

    #create a substring from first part of name, and make it uppercase
first_name=name[0:3].upper()    #or [:3]
print(first_name)

    #create substing of last name, and make it lowercase
last_name=name[4:]. lower()
print(last_name)

    #negative indexing
last_character=name[-1]
print(last_character)

"""
"""

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

"""
"""

#22 Return Statement - in 21 we sent values to the function
#                       now we will have function send values back to the caller

def multiply(number_1, number_2):   #defining function
    #result=number_1*number_2   #remove this for less lines of code
    #return result
    return number_1*number_2 

multiply(6, 8)      #doesnt print anything

print(multiply(6, 8))

x=multiply(6, 8)
print(x)

"""
"""

# 23 Keyword arguments - arguments passed to a function have an identifier
#                       - order of arguments does not matter, unlike positional arguments

def hello(first,middle,last):
    print("hello "+ first+" "+middle+" "+last)
    
    #the below is positional argumets, the order in which arguments are passed matters when we call this function
hello("Bro", "Dude", "Code")

    #below is keyword arguments
hello(last="Code", middle="Dude", first="Bro")

"""
"""

#24 nested function calls - function calls inside other function calls
#                           innermost function calls resolved first
#                           returned value is used as argument for the outer function

num=input("Enter a whole positive number: ")
num=float(num)      #turn to float because when you accept user input, remember its a string
num=abs(num)
num=round(num)
print(num)

    #nested function calls let you do in 1 line of code
print(round(abs(float(input("Enter a whole positive number: ")))))

"""
"""

#25 variable scope 
#   scope is the region that a variable is recognized in
#   a vriable is only available from inside the region in which it is created
#   there is local and global variables

def display_name():      #created function
    name = "Code"       #variable created and available inside function, local scope
    print(name)
#print(name)        #cant do this because we are not inside the above function

name="Bro"      #this is a global scope variable, available inside and outside functions

display _name()      #displays local name variable
print(name)         #displays global name variable

#   if you did not creat a local variable inside the above function, then when you called display_name()
#   it would show the global variable name. 
#   order is LEGB, program uses local variables, then enclosing variable, then global variables, then built in variables

"""
"""

#26 args - parameter that will pack all arguments into a tuple
#          useful so that a function can accept a varying amount of positional arguments

def add(num1, num2):
    sum=num1+num2
    return sum
#print(add(1, 2, 3)) #cant do this bc my function only accepts 2 parameters
   
    #to allow any number of arguments, do as below
def add(*args):     #can replace args with another label
    sum=0
    args=list(args)   #cast touble into list so we can change a certain value. touble doesnt support item assignmet
    args[0]=0
    for i in args:
        sum+=i
    return sum
print(add(1, 2, 3, 4, 5, 6))

"""
"""

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

"""
"""

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

"""
"""

# 29 random numbers using random module.
    #need to import random library for this: import random

x=random.randint(1,6)       #rando int within a specified range
y = random.random()         #random floating number btween 0 and 1

myList = {'rock', 'paper', 'scissors'}      #use with a list or other collection
z=random.choice(myList)

cards=[1,2,3,4,5,5,6,7,8,9,10,"j","q","k","a"]
random.shuffle(cards)

print(x)
print(z)
print(cards)

"""
"""

#30 Exception Handling - events deected during execution that interrupt the programs flow     
    #in the below program, if the denom etered is 0, we will get an interruption
    #we will get an exception, we need to handle these somehow
numerator = int(input("enter a number to divide: "))
denominator = int(input("Enter a number to divide by: "))
result = numerator / denominator
print(result)

    #one way to deal with exception is to put anything that might cause this error into a try block
try:    
    numerator = int(input("enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError:       #if input for denom was 0
    print("you cant divide by 0 idiot")
except ValueError as e:              #if input got letters, use the as e and print(e) to print to console what the error was
    print(e)
    print("enter only numbers please")
except Exception:               #Exception is general, it accouts for all interruptions
    print("somehting went wrong: ")
else:                           #execuutes if no exceptions are caught
    print(result)
finally:                        #the finally clause will always execute
    print("This will always execute")

"""
"""

# 31 file detection
    #import the os module: import os

path="C:\\Users\\Hasaan\\Documents\\Python\\test.txt"    #save a file path in a variable, #use double back slashes, bc thats the escape sequence for a backslash in a string

if os.path.exists(path):                #check if the location exists
    print("That location exists: ")
    if os.path.isfile(path):            #check if the lacation stores a file, could also be a folder for example
        print("that is a file")
    elif os.path.isdir(path):           #check if location stores a folder
        print("that is a directory")    
else:
    print("That location doesnt exist")

"""
"""

#32 Read a files contents
    #This automatically closes files after opening them
    #Good to add exception handling
try:
    with open('C:\\Users\\Hasaan\\Documents\\Python\\test.txt') as file:    #could also put  open('test.txt') since its in same project folder as this script
        print(file.read())
except FileNotFoundError:
    print("that file wasnt found")
    
print(file.closed)  #checks that file is closed

"""
"""

# 33 Writing to files 
    #the open function allows you to ass in 2 arguments
    #by default there is an r for read open('C:\\Users\\Hasaan\\Documents\\Python\\test.txt', 'r')
    # add 'w' to write to file, this will overwrite itself 
    # add 'a' to append file
text="OMG\nthis is some text\nhave a good one\n"
with open('test.txt', 'w') as file:
    file.write(text)

text2="Im going to add a bit to the end, see ya!"
with open('test.txt', 'a') as file:
    file.write(text2)

"""
"""

# 34 Copying a file
    #import the shutil module. there are others ways this is what we will use
    #this module has 3 basic functions
        # copyfile() - copys contents of a file
        # copy() - copyfile()+permission mode+destination can be a directory
        # copy2() - copy() + copies metadata (files creation and modification times)
    #all 3 above functions use the same 2 arguments

shutil.copyfile('test.txt', 'copy.txt') #2 arguments(source, destination) if its in same project, then add file name, it its elsewhere add the path

"""
"""

# 35 Move a file or directory(folder)
    #import os module

text="OMG\nthis is some text\nhave a good one\n"
with open('move.txt', 'w') as file:
    file.write(text)

source="move.txt"
destination="C:\\Users\\Hasaan\\Documents\\Python\\movecomplete.txt"    #you ae moving move to your python folder and renaming movecomplete, remember you need to use double \\

try:
    if os.path.exists(destination):    #check if there is already a file there
        print("there is already a file here")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+ " was not found")

"""
"""

# 36 Delete File or directory
    #import os module
    # first you added a text file to project and called it delete(right click project in your workspace>new file)
    # you also created a folder called empty
    #you also created a folder called deletefolderwithfile and added a file to that folder
    #we will use try block for exception handling, not necessary

path="delete"       #file
try:
    os.remove(path)
    # or like this: os.remove('delete.txt')
except FileNotFoundError:
    print("File not found")
else:
    print(path + " was deleted")
    

#deleting empty folder requires another function, you cant use os.remove
path2="empty"            #empty folder
try:
    os.rmdir(path2)
except FileNotFoundError:
    print("File not found")
except PermissionError:                         #if you try to delete the empty folder, that requires another function
    print("you do not have permission to delete that")
else:
    print(path2 + " was deleted")

#to delete a folder with files you need import shutil module
path3="deletefolderwithfile"    #folder with file(s)
try:
    shutil.rmtree(path3)
except FileNotFoundError:
    print("File not found")
except PermissionError:                         #if you try to delete the empty folder, that requires another function
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete a directory with files using rmdir function")
else:
    print(path3 + " was deleted")

"""
"""

# 37 NOT FINISHED, RETURN TO THIS LATER
#37 Modules - a file containing python code. may contain functions, classes, etc.
            #used with modular progrmming, which is to seperate a program into parts
            #right clisk project>new>python file

"""
"""

# 38 Rock Paper Scissiors Game - in new file
# 39 Quiz Game - in new file

"""
"""

#40 Object Oriented Programming, #41 Class Variables
    # an object is an instance of a class
    #you can create a new class here or you could create it in a seperate module and import it here
    #objects hve attributes and methods(what object can do)
    #class variable set all instances of the class, all car objects. so all car objects will have 4 wheels. 
    #Instance variable are deined inside the constructor(inside this: def __init__(self, make, model, year, color):), can differ for all objects, class variable dont differ
class Car:         #object

    wheels= 4   #class variable

    def __init__(self, make, model, year, color):      #special method that constructs objects for us
        self.make=make   #attribute. Instance variable. self. refers to the object we are surrently woking on/creating
        self.model=model    #instance variable
        self.year=year  #instance variable
        self.color=color    #instance variable

    def drive(self):        #Method. self is 1 argument, it refers to the object using this method
        print("This " +self.model+ " is driving")
    
    def stop(self):
        print("This "+self.model+" has stopped")


car_1 = Car ("Chevy", "Corvette", 2021, "blue") #you dont need to pass anyhting for the self argument, this is done automatically
car_2 = Car ("Ford", "Mustang", 2022, "red") #you dont need to pass anyhting for the self argument, this is done automatically

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()           #see how () is empty you did not call self
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()           #see how () is empty you did not call self
car_2.stop()

car_1.wheels = 2        #you can change the clas variable for a particular object
print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)       #(name of class, name of class variable) to display its value
#print(Car.color)       #cant do this because its an instance varioable

Car.wheels=2 #this will change the class variable for all instances of the class
print(car_1.wheels)
print(car_2.wheels)

"""
"""

#42 Inheritance - classes can inherit attributes or methods from another class
    # child class wil recieve eveyhting from parent class

class Animal:       #creating parent class
    alive=True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Rabbit (Animal):  # here you are saying Rabbbit is the child of Animal class, so it will inherit everyhting from animal class
    def run(self):
        print("this rabbit is runnning")
class Fish(Animal):
    def swim(self):
        print("this fish is swimming")
class Hawk(Animal):
    pass

rabbit=Rabbit()     #creating object rabbit from classes
fish=Fish()
hawk=Hawk()

print(rabbit.alive) #this has alive because we used inheritance
fish.eat()      #got this method from inheritance
hawk.sleep()    #got this method from inheritance

rabbit.run()
fish.swim()

"""
"""

#43 Multi level inheritance - when a child class inherits another child class

class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        print("this animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog=Dog()       #creating dog object
print(dog.alive)
dog.bark()
dog.eat()

"""
"""
#44 multiple inheritance - child class is derived from more than 1 parent class

class Prey:

    def flee(self):
        print("This animanl flees")
    
class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()
#type fish. , hawk. , rabbit. to see all the classes it has access to

"""
"""

# 45 Method Overiding - child class provides a specifir implementtion of a method it has inherited 
    #see the eat class is overwritten specifically in cls rabbit.
class Animal:
    def eat(self):
        print("this animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()

"""
"""

#46 Method Chaining - calling multiple methods sequencially
    #each call performs an action on the same object and returns self
    #if you want to use method cahining you have to return something, because pyhon automatically returns none

class Car:
    def turn_on(self):
        print("you start the engine")
        return self
    
    def drive(self):
        print("you drive the car")
        return self

    def brake(self):
        print("you step on the brake")
        return self
    
    def turn_off(self):
        print("you turn off the engine")
        return self

car=Car()
car.turn_on()
car.drive()

    #i want to call these 2 sequencially, but to do below i will have to add return statements
car.turn_on().drive()   #without adding the return stemements you get this error: AttributeError: 'NoneType' object has no attribute 'drive'

"""
"""

#47 Super Function - function used to give access to the methods of a parent class
    #returns a temporary obect of a parent class when used


class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)     #Thsuper function asks the rectangle clas if we can use its method

    def area(self):
        return self.length*self.width
    
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height=height

    def volume(self):
        return self.height*self.length*self.width

square=Square(3, 3)
cube=Cube(3,3,3)

print(square.area())
print(cube.volume())

"""
"""

# 48 Abstract class
        #prevents user from creating an obect of that class
        #and compels user to override abstract methods in a child class
        #from abc import ABC, abstractmethod   : add this to beginning of program
            #Abstracts class: contains 1 or more abstract methods
            #Abstract method: methods has a declaraation but no implementation

#imagine that for a game you want the player to make an object of the car class 
#or mortorcycle class, but not from vehicle class because thats too generic.
#so we will make vehicle class abstract

class Vehicle(ABC):     #vehicle class inherits from ABC class. for all methods here add @abstractmethod
    @abstractmethod     #you cant remove this abstract method, bc then you can still create a vehicle object bc you need at least 1 abstract method
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

class Mortorcycle(Vehicle):
    def go(self):                     #if you forgot to add the go method to motorycle class you would get an error. child class must implement the parent abstract method
        print("You ride the mortorcycle")

#vehicle=Vehicle()      :gives error-TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract method 'go'  
car=Car()
motorcycle=Mortorcycle()

#vehicle.go()
car.go()
motorcycle.go()

"""
"""

# 49 Objects as Arguments
        # you can pass objects as arguments

class Car:
    color = None

class Mortorcycle:
    color = None

def change_color(car, color):      #seperate function (not method of clar class) outside of car class. want 2 parameters: car object and color. the name of parameter that accepts the car object (car) can be named smething else. just keep it lowercase, argument names should be lowercase
    car.color=color

car_1=Car()
car_2=Car()
car_3=Car()

bike_1=Mortorcycle()

print(car_1.color)
print(car_2.color)
print(car_3.color)

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

"""
"""

# 50 Ducktyping - concept where the class of an object is less important than
        # the methods or attributes of the class.
        #class type is not checked if minimum methods/attributes are present
        #if it walks like a duck, and quacks like a duck it must be a duck

class Duck:
    def walk(self):
        print("this duck is walking")
    
    def talk(self):
        print("this duck is qwacking")

class Chicken:
    def walk(self):
        print("this chicken is walking")
    
    def talk(self):
        print("this chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")

duck=Duck()
chicken=Chicken()
person=Person()

person.catch(duck)
person.catch(chicken)   #this works  bc python is seeing the same methods so it lets you pass an object of another class. chicken can walk and talk like duck so its basically a duck
                        #if chicken had different methods or was missing a method that duck has this would not work

"""
"""

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

"""
"""

# 52 Assign function to variable

def hello():
    print("Hello")

print(hello)        #when you print function, the output shows the location of the function within computers memory - this loction can change everytime you run

hi=hello            #assign function address to variable hi
print(hi)           #prints same address as hello, have the same memory address

    #if you call hi functon, you will accc call the helllo funciton.
    #hello function  basically has 2 names hello and hi
hello()
hi()

say=print   #print function being saved to variable say
say("Whoa! this works :O")      #now you can use say instead of print to print something

"""
"""

# 53 Higher order functions - a function that either
#                             1. accepts a function as an arguemnt 
#                                           or
#                             2. returns a function
#                             (in python, functions are also treated as objects)
    #1. accepts function as an arument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):        #passing in a function, could be loud or quiet, so we use arbitrary name func
    text=func("Hello")
    print(text)

hello(loud)     #call loud into hello function
hello(quiet)

    #2. retuns a function
def divisor(x):         #we passed in divisor(2) so x is 2
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))

"""
"""

# 54 lambda functions
#       -function written in one line and use lambda keywrd
#       -accept any number of arguments, but only has one expression
#       (think of it as a shortcut)
#       (useful if needed for a short period of time, throw-away)
#lambda parameters:expression

def double(x):
    return x*2
print(double(5))

double = lambda x:x*2   # does the same as above using lambda function
multiply = lambda x, y:x*y
add=lambda x, y, z :x+y+z
full_name=lambda first_name, last_name: first_name+" "+last_name
age_check=lambda age: True if age>= 18 else False

print(double(5))
print(multiply(5, 6))
print(add(5, 6, 7))
print(age_check(18))

"""
"""

# 55 sort iterables
        #sort() method= used for lists only
        #sort() funtion= used with iterables (lists, touples, etc)

#sort method
students = ["Squidward", "Sandy", "Parick", "Spongebob", "Mr.Krabs"]    #list
 
    #sort list in alphabetical order
students.sort()
for i in students:
    print(i)

    #sort list in reverse alphabeticaal order
students.sort(reverse=True)
for i in students:    
    print(i) 

#sort function
students2=("Squidward", "Sandy", "Parick", "Spongebob", "Mr.Krabs")   #touple

sorted_students=sorted(students2)   #returns a list: sorted_students=, but allows you to sort a touple
for i in sorted_students:    
    print(i) 

sorted_students=sorted(students2, reverse=True)   #sorts in everse order
for i in sorted_students:    
    print(i) 

#more complicated example- list of touples (name, grade, age)
students3=[("Squidward", "F", 60),
           ("Sandy", "A", 33),
           ("Squidward", "D", 36),
           ("Squidward", "B", 20),
           ("Squidward", "C", 78)]


students3.sort()    #sort alphabetically. by default sorts by first column which is the name here

    #if we want to sort by grade or name we can use keyword arguments. here we sort by grade
grade=lambda grades:grades[1]       #set index of 1 for first column. index 0 is the name, 1 is the grade, 3 is the age
students3.sort(key=grade)

for i in students3:    
    print(i) 

#sort by age
age=lambda ages:ages[2]       #set index of 1 for first column. index 0 is the name, 1 is the grade, 3 is the age
students3.sort(key=age)
#students3.sort(key=age, reverse=True)

for i in students3:    
    print(i) 


#more complicated example- touple of touples (name, grade, age)
#since its ouple, cant use sort function as that belongs to lists only
students4=(("Squidward", "F", 60),
           ("Sandy", "A", 33),
           ("Squidward", "D", 36),
           ("Squidward", "B", 20),
           ("Squidward", "C", 78))
age=lambda ages:ages[2]
sorted_students=sorted(students4, key=age)

for i in sorted_students:
    print(i)

"""
"""

#56 Map  - applies a function to each item in an iterable (list touple, etc)
# map()
# map (function, iterable)

store=[("shirts", 20.00),
       ("pants", 25.00),
       ("jacket", 50.00),
       ("socks", 10.00)]

    #to convert the above prices to euros or dollars
to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars=lambda data: (data[0], data[1]/0.82)
#store_euros=map(to_euros, store)   #map function will create a map object
store_euros=list(map(to_euros, store))  #but you could cast that to a different type of iterable
store_dollars=list(map(to_dollars, store)) 

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)

"""
"""

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

"""
"""

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

"""
"""

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

"""
"""

# 60 Dictionary Comprehension - create a dictionary using an expression
                                #can replace for loops and certain lambda functions
                                #dictionary = {key: expression for (key, value) in iterable}
                                #dictionary = {key: expression for (key, value) in iterable if conditional}
                                #dictionary = {key: (if/else) for (key, value) in iterable}
                                #dictionary = {key: function(value) for (key, value) in iterable}


cities_in_F = {'New York':32, 'Boston':75,'Los Angeles':100, 'Chicago':50 } #created dictionary. city names are keys. tem in farenheit are values

#we gonna create a seperate dictionary that has the tem in celcius using dictionary comprehension. also we added round function
cities_in_C={key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

#example using an if conditional
weather = {'New York': "snowing", 'Boston':"sunny", 'Los Angeles': "sunny"}
sunny_weather= {key: value for (key, value) in weather.items() if value =="sunny"}

print(sunny_weather)

#exaple with if/else conditional
cities = {'New York':32, 'Boston':75,'Los Angeles':100, 'Chicago':50 } #created dictionary. city names are keys. tem in farenheit are values
desc_cities={key: ("warm" if value >= 40 else "COLD") for (key, value) in cities.items()}

#emample calling a function
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69>=value>=40:
        return "WARM"
    else:
        return "COLD"

cities2 = {'New York':32, 'Boston':75,'Los Angeles':100, 'Chicago':50 } #created dictionary. city names are keys. tem in farenheit are values
desc_cities2={key: check_temp(value) for (key, value) in cities2.items()}

print(desc_cities2)

"""
"""

# 61 Zip function - aggregates elements from 2 or more iterables(list, tuples, sets, etc.)
                    #creates a zip object with paired elemens stored in tuples for each element
                    # zip(*iterables)
usernames = ["Dude", "Bro", "Mister"]       #list of usernames
passwords = ("p@ssword", "abc123", "guest") #tuple of passwords
login_date=["1/1/2021", "1/2/2021", "1/3/2021"]

#users is the zip object. zip objects are iterable
users = zip(usernames, passwords)   #we have created a zip object of tuples, and each touple is storing a pair from the 2 iterables we provided

print(type(users))
for i in users:
    print(i)

users2 = list(zip(usernames, passwords))    #you can cast it to a list. now we have a list of tuples. each tuples is storing a pair

print(type(users2))
for i in users2:
    print(i)

users3 = dict(zip(usernames, passwords))    #since we are only passing in 2 iterables, we can cast as dictionary, so its storing key value pairs

print(type(users3))
for key, value in users3.items():
    #print(key, value)
    print(key+" : "+ value) #add colon for readability

#example with 3 iterables
users4=zip(usernames, passwords, login_date)
for i in users4:
    print(i)

"""
"""

# 62 NOT WORKING RIGHT NOW, RETURN TO THIS LATER. UNFINISHED
# 62 if __name__=='__main__:'
        # y tho?
        # 1. Module can be run as a standalone program
        # 2. Module can be imported and  used by other modules

        # Python interpreter sets "special variables", one of which is __name__
        #then python will execute the code found in __main__

        #python files are also referred to as modules. by including this statement, it gives our modules
        #some flexibility, see 1 and 2 above
if __name__=='__main__':  #this statement checks to see if the user is runing this module as a standalone program, or its being imported from other modules
    pass

            #behind the scenes the python interpreter sets "special variables" one of which is __name__
            #python will assign the __name__ variable a value of '__main__' if its
            #the initial module being run

print(__name__) #since i am running this from this module/file, it will print __main__

import module_2
print(module_2.__name__)

"""
"""

# 63 time module
    # import time module

print(time.ctime(0))        #print epoch - a date and time from which a computer measures system time
                            #kinda like the date/time your computer thinks time began, used as a reference point
                            #vary based on computer/OS
                    
                            #converts a time expressed in seconds since epoch to a readable string

print(time.ctime(1000000))  #returns the data/time 1000000 after epoch

print(time.time())          #return how many seconds passed since epoch at the time program is ran

print(time.ctime(time.time()))  #combine above 2 methds to get crrent date and time

#another way to get current date/time
time_object = time.localtime()      #localtime method creates a time object based on curent time so time_object is a time object variable
print(time_object)      #you can change formatting to be more readable, we will use strftime(format, timeObject) function to help

#time.strftime(format, time_object)   #takes format nd time object as arguments
                                    #format is a string of different directives: see python official documentation on time module strf time function
                                    # many different directives that represent different time formats, see documentation to pick the type of formatting you want
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) 
print(local_time)

#you can also get UTC time: Coordianted Universal TIme is the primary time standard by which the world regulates clocks and time
time_object2 = time.gmtime()
print(time_object2)

#strp time function - parses a string representation of a time and/or date and return a time object
time_string="20 April, 2020"
#time.strptime(string, format)          accepts 2 arguments(time represented as string, and telling the computer the formating directives of the time string, this function creates a time object
time_object3=time.strptime(time_string, "%d %B, %Y")
print(time_object3)      #output is not so east to read, you can change that as we learned earlier

#asctime(t) function - accepts 1 arument: a tuple representation of a time
#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst). dst is -1 or 0
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string=time.asctime(time_tuple)
print(time_string)

#mktime(t) function - accepts 1 arument: a tuple representation of a time or a time object and converts it to a seconds since epoch
#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst). dst is -1 or 0
time_string2=time.mktime(time_tuple)
print(time_string2)

"""
"""

# 64 threading, multithreading
        #thread - is a flow of execution. each thread can carry out a seperate order of instructions
        #multithreading allows us to run different parts of a program at different times
        #each thread takes a turn running due to GIL to achiece concurrency
        
        #GIL = global interpreter lock
        #allows only one theard to hold the control of the pythin interpreter at any one time

#programs and tasks can be divided into 2 caegores: cpu bound, io bound  
   
    #cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
    # use multiprocessing

    #io bound = program//task spends most of its time waiting for external events (user input, web scraping)
    # use multithreading

#import threading
#import time

#an example where mutithreading is used is in that quiz game you made earlier
#you could have had a count down going while waiting fro user input (io bound task)
#1 thread would be waitng for user input and 1 thread would be in charge of a countdown timer
#2 threads would be running concurrently in above example


#imagine you have 3 tasks to complete in the morning before work

def eat_breakfast():
    time.sleep(3)           #time takes 3 seconds
    print("you finished breakfast")

def drink_coffee():
    time.sleep(4)
    print("you finished coffee")

def study():
    time.sleep(5)
    print("you finished studies")

#these tasks are spending time waiting for externl events, waiting for the sleep functions to expire
#below we complete these tasks sequencially not concurrently
#we have 1 thread in charge of the three seperate functions here
#eat_breakfast()
#drink_coffee()
#study()


#lets get these function running concurrently: because humans can multitask
#lets create 3 thread, each thread in charge of each task with main thread reunning in background to complete the rest of the program
#main thread just runs like normal, start immediatly and runs like normal. its not taking care of these 3 function but its going to run the enumerate and active call, perf_counter functions normally

x=threading.Thread(target=eat_breakfast)
#x=threading.Thread(target=eat_breakfast, args=(1,))       if your function had arguments that need to be passed in, add in the arguments followed by a comma
x.start()       #to start the thread

y=threading.Thread(target=drink_coffee)
y.start()

z=threading.Thread(target=study)
z.start()

#there is something called thread synchronization, we can have the main thread wait for another thread to finish before completing its instruction
x.join()    #now main thread has to wait for these threads to synchronize to move on with its own instruction
y.join()
z.join()

#whenever we run a program we have one thread running that is in chanrge of executing our program
#we can count the number of threads currently active in the background
print(threading.active_count()) #prints number of active threads in program

print(threading.enumerate())    #prints a list of all threads that are running

print(time.perf_counter())  #tells us how long it takes our calling thread (main thread) to finish its set of instructions

"""
"""

# 65 daemon threads
            #a thread that runs in the background, not important for the program to run
            #your program will not wait for daemon threads to complete before exiting
            #non daemon threads cannot normally be killed, stay alive until task is complete

            #ex. background tasks, grbage collection, waiting for input, long running process

#import threading
#import time

#we have 2 threads, our main thread will wait for user input, in the backgroud we will have a thread with a timer dislaying how long someone is logged in
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count,"seconds")

#x=threading.Thread(target=timer)       #normal thread
x=threading.Thread(target=timer, daemon=True)   #daemon thread
x.start()

#x.setDaemon(True)  this method lets you set false or true depending on if you want it to be daemon or non daemon
                    #you cant change it if its currently running, this needs to be set before the start function

#print(x.isDaemon)   #return whether or not the thread is a daemon thread


answer=input("do you wish to exit?")

#now with normal threads even if you put some input and hit enter, the main thread is complete
#but my background timer is still going
#what if i want to to close the program?
#non daemon threads cannot normally be killed, stay alive until task is complete
#for this i will need to use daemon threads

"""
"""

# 66 THIS IS NOT WORKING FOR ME, RETURN TO THIS
# 66 Multiprocessing - running tasks in parallel on different cpu cores, bypasses GIL used for threading
                        #multiprocessing = better for cpu bound tasks (heavy cpu usage)
                        #mutithreading = better for io bound tasks(waiting around) - limited to running 1 thread at a time bc of GIL

#from multiprocessing import Process, cpu_count
#import time


def counter(num):       #this is the function we will call with the processes we create. child process
    count=0
    while count<num:
        count+=1

def main ():
    a= Process(target=counter, args=(10000,))  #create a process, for arguments you have to pass in  tuple. 
    a.start                                            #since we only have 1 rgument to pass in, to diffrenciate from an expression we add a comma at the end
    a.join()            #main process will wait for child process before continuing

    print("finished in: ",time.perf_counter(), "seconds")

# if you are running windows processing sytem, add the below line because
#when we run  program we have a main process that is runnning
#if we create a child process from that process, its going to copy the module we are working with
#that child process will create its own children process and this can be a problem
if __name__ == 'main':
    main()

"""
"""

#67 GUI Windows
from tkinter import *       #imports everything related the tkinter module

#windows = serves as a container to hold or contain these widgets
#widgets = GUI elements: buttons, textboxs, labels, images

#we will create a new window
my_window=Tk() #instanciate an instance of a window for us

#we want to customize the appearance of the window
my_window.geometry("420x420")       #set the size of the window

my_window.title("Bro Code first GUI program")       #retitles the window from tk

#change the icon of the window bar at the top from feather icon
#copy paste image into your project folder. the image format is currently unreadable for Tkinter
#we need to convert our image into a photo image
icon_photoimage=PhotoImage(file='image.png')        #converts our image to  photo image, can also get image from desktop with file path
my_window.iconphoto(True, icon_photoimage)      #this sets the icon image, 2 arguments(True, name of your photoimage). true is always set to true.

my_window.config(background='Black')                   #change the background color of the window
my_window.config(background="#5cfcff")                  #can also change backgroung clor with a hex value, add a # before the hex color code

my_window.mainloop()       #to display the window, place window on computer screen, listen for events

"""
"""

# 68 Labels = an rea widget that holds text and/or an image within a window
from tkinter import *       #imports everything related the tkinter module

my_other_window = Tk()

my_photo_image=PhotoImage(file='image.png')  #get your photo image to add image to your label

my_label=Label(my_other_window, 
               text="Hello World", 
               font=('Arial', 40, 'bold'), 
               fg='#00FF00', 
               bg='black', 
               relief=RAISED, 
               bd=10, 
               padx=20, 
               pady=20,
               image=my_photo_image     #adds our photo image to label, but replaces all our text so we need to use compound option to place it
               compound='top'           #compound='botton' : image appears underneath out text. compound='top' image is places above our text.
               )
                 

#label constructor. label only takes up the room it needs
#arguments are: (master/container(the name of the window that will contain the label), you can add more arguemnts for customization) 
#Sample arguments
#text="text you ant on label"
#font=('Arial', 40, bold)
#fg is foreground which is the font color. can add hex or text value here. fg='#00FF00'
#bg is background color
#relief sets the border style. add a border around label. there is RAISED and SUNKEN
#bd changes the border width, default is 1
#padx and pady :we can also add padding between text and border


my_label.pack()                 #by default places you widget/label to the top center of the container
#my_label.place(x=0, y=0)        #change the coordinates of where the label is placed

my_other_window.mainloop()

"""
"""

# 69 Buttons = you click it, then it does stuf
from tkinter import *       #imports everything related the tkinter module

count=0                     #variable to count number of times button is clicked

def click():
    global count            #you need to add that its global : im not sure why, find out
    count+=1
    print(count)

window=Tk()

photo=PhotoImage(file='image.png')

button = Button(window,                     #button constructor(master, other arguments)
                text="click me",            #add text on button
                command=click,              #we need to set a command to make the buton do something. we need to give command a function name. this is called a call back because you give it the function name without the parenthesis
                font=("Comic Sans", 30),    #change font of button, and size of button
                fg="#00FF00",               #set the foreground color (font color). put color name or hex code
                bg="black",                 #background color
                activeforeground="#00FF00", #activeforeground, activebackground. allow you to select color scheme for hile button is pressed. you have set some specifications for how the button color should look, when you click the button the color scheme changes while the button is pressed
                activebackground='black',
                state=ACTIVE,               #state can be ACTIVE or DISABLED. DISABLED if you need to disable someone from clicking on this button
                image=photo,                 #to add an image to a button, however this will replace the text                                           
                compound='bottom' #use to have text an image on the button
                )     

button.pack()       #displays the button

window.mainloop()

"""
"""

# 70 Entrybox
#       entry widget = textbox that accepts a single line of user input
from tkinter import * 

def submit():
    username=entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)            #this allows you to disable the entry box after 1 username input, you can also set ACTIVE or DISABLED in constructor, see button example above

def delete():
    entry.delete(0, END)     #this delete function takes 2 arguments (whats the firsrt character to remove, last character to remove) so (0,END) takes first character to the end nd deletes it. <Name of entry box>.delete

def backspace():
    #entry.delete(END-1, END)
    entry.delete(len(entry.get())-1, END)      #get the second to last character by get the length of all characters in entry box and -1 from it

window=Tk() #creating window

entry = Entry(window,#constructor(master, other arguments)
            font=("Arial", 50),
            fg='#00FF00',       #foreground color, test color
            bg="black"          #background color
            show="*"            #when user put input in entrybox, you cn set it so that only a specific character shows on screen, if hey enter a password, only asterisks are visible
            )

#adding default text to entry box (<Positional argument:where to start the text>, "<text to display>" )
entry.insert(0, "Spongebob")



entry.pack(side=LEFT)       #displays the entrybox. side left you position it on left or right side

submit_button= Button(window, text="submit", command=submit)    #creating a submit buton to make use of entrybox
submit_button.pack(side=RIGHT)

delete_button= Button(window, text="delete", command=delete)    #creating a submit buton to make use of entrybox
delete_button.pack(side=RIGHT)

delete_backspace= Button(window, text="backspace", command=backspace)    #creating a submit buton to make use of entrybox
delete_backspace.pack(side=RIGHT)

window.mainloop()

"""
"""

# 71 Checkbox/Checkbuttons 

from tkinter import*

def display():
    if(x.get() == 1):          # if x was storing boolean do if(x.get()): this will return true or false. if x was storing string do if(x.get()=="YES"):
        print("You agree")
    else:
        print("You dont agree :(")

window=Tk()

x=IntVar()      #IntVar(). if the variable x returned a string we would do x=StringVar(). if returned boolean do x=BooleanVr(). you would use onvalue and offvalue in constructor to change it to store a string, by default it stores 1 and 0
                #IntVar() is a variable in clas Tkinter. holds integer values for varios widget operations
                #should be created within the instance of the window

photo_photoimage=PhotoImage(file="image.png")

check_button = Checkbutton (window,
                            text="I agree to smth",
                            variable=x,      #associating variable with checkbutton, checkbutton stores 1 or 0 by default
                            #onvalue=1,      #lets you change what value represents on. by default it uses 1 for on and 0 for off
                            #offvalue=0,
                            command=display,
                            font=('Arial', 20),
                            fg='#00FF00',
                            bg='black',
                            activeforeground='#00FF00',
                            activebackground='black',
                            padx=25,
                            pady=10,
                            image=photo_photoimage,
                            compound='left')        #placing image left of text

check_button.pack()

window.mainloop()

"""
"""

# 72 Radio Buttons = similar to checkbox but you can only select 1 from a group
from tkinter import*

#makeing a list
food=["pizza", "hamburger", "hotdog"]

def order():
    if (x.get()==0):
        print("you ordered pizza")
    elif (x.get()==1):
        print("you ordered hamburger")
    elif (x.get()==2):
        print("you ordered hotdog")
    else:
        print("huh?")

window=Tk()

x=IntVar()      #should be created within the instance of the window

pizzaImage=PhotoImage(file='image copy.png')
HamburgerImage=PhotoImage(file='image copy 2.png')
HotdogImage=PhotoImage(file='image copy 3.png')
foodImage=[pizzaImage, HamburgerImage, HotdogImage]

for index in range(len(food)):           #will iterate once through all lements in our list, will create 3 radiobuttions for us
    radiobutton=Radiobutton(window, 
    text=food[index],       #adds text to radio buttons
    variable=x,             #since x is associated with all the list elements, when you select 1 checkbox you automatically select them all, same thing when you deselect...Groups radiobuttons together if they share a variable
    value=index,            #asssigns each radiobutton a different value. we need to give each radion button its own value, so make value=index
    padx=25,                #adds padding on x axis
    font=("Impact", 50),
    image=foodImage[index],     #adds image to radiobutton
    compound = "left",     #adds image left of text
    indicatoron=0,      #eliminates circle indicators
    width=375,     #sets width of radiobuttons
    command=order   )    #set command of radiobuton to funtion
    radiobutton.pack(anchor='w')    #by default radiobuttons are centered, lets anchor them to the West

window.mainloop()


"""
#"""

# 73 Scale





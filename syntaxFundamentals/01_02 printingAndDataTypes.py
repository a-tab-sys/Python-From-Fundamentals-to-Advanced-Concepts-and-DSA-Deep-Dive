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
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
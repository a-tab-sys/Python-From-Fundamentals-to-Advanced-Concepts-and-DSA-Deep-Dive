#06 Accepting user input
input("wht is your name? ")

    #save to variable
name1=input("wht is your name? ")
print("hello "+ name1)

    #default input is string, you need to type cast to diff data type to do calculations on inputted data
age=input("How old are you?: ")
#age= age + 1                           #wont work because you are doing calc on a string and int 
print("your age is: "+age)
    
    #instead we can use type casting when accepting input
age2 = int(input("How old are you?: "))         #use float instead to accept decimal inputs
age2=age2 + 1
#print("your age is"+age2)                      wont work bc you are concatenating a string and int
print("your age is: "+str(age2))
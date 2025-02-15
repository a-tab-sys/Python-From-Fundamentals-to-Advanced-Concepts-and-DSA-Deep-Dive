#25 variable scope 
#   scope is the region that a variable is recognized in
#   a vriable is only available from inside the region in which it is created
#   there is local and global variables

def display_name():      #created function
    name = "Code"       #variable created and available inside function, local scope
    print(name)
#print(name)        #cant do this because we are not inside the above function

name="Bro"      #this is a global scope variable, available inside and outside functions

display_name()      #displays local name variable
print(name)         #displays global name variable

#   if you did not creat a local variable inside the above function, then when you called display_name()
#   it would show the global variable name. 
#   order is LEGB, program uses local variables, then enclosing variable, then global variables, then built in variables


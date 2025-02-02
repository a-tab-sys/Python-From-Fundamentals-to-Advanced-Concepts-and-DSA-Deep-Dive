# 23 Keyword arguments - arguments passed to a function have an identifier
#                       - order of arguments does not matter, unlike positional arguments

def hello(first,middle,last):
    print("hello "+ first+" "+middle+" "+last)
    
    #the below is positional argumets, the order in which arguments are passed matters when we call this function
hello("Bro", "Dude", "Code")

    #below is keyword arguments
hello(last="Code", middle="Dude", first="Bro")
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
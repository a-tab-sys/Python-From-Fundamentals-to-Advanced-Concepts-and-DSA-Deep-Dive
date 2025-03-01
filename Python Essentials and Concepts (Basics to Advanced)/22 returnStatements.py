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
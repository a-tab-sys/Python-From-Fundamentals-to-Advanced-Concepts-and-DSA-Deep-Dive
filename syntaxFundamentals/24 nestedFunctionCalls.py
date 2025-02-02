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

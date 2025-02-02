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

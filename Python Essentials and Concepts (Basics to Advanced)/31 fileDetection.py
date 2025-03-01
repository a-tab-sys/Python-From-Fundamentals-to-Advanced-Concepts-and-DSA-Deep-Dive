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

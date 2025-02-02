#32 Read a files contents
    #This automatically closes files after opening them
    #Good to add exception handling
try:
    with open('C:\\Users\\Hasaan\\Documents\\Python\\test.txt') as file:    #could also put  open('test.txt') since its in same project folder as this script
        print(file.read())
except FileNotFoundError:
    print("that file wasnt found")
    
print(file.closed)  #checks that file is closed

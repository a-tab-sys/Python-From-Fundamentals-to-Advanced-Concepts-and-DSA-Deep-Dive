#11 While Loops - will excecute code, as long as its condition is true
name=""
while len(name) ==0:            #while the length of the name is 0
    name = input("enter your name: ")
print("Hello "+name)

    #another way to write the above
name2=None
while not name:
    name=input("enter your name: ")
print("Hello "+name)
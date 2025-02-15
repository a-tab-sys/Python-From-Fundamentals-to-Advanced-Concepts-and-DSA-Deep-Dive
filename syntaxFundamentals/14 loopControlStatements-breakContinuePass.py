#14 Loop control statements (break, continue, pass)
    #break = used to termainate loop entirely
    #continue = skips to next iteration of loop
    #pass = does nothing, acts as a placeholder

    
    #break statement - used to termainate loop entirely
    #program continually asks for name until one is entered, once one is entered it breaks
while True:
    name = input("Enter your name: ")
    if name != "":
        break
 
    #program removes dashed from phone numbers
    #continue statement - skips to next iteration of loop
phone_number = "123-456-7890"
for i in phone_number:
    if i=="-":
        continue
    print(i, end="")

     #pass = does nothing, acts as a placeholder
     #prints all numbers except 13
for i in range(1, 21):
    if i ==13:
        pass
    else:
        print(i)
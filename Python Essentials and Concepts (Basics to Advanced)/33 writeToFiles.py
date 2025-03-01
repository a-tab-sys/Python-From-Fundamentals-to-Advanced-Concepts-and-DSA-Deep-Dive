# 33 Writing to files 
    #the open function allows you to ass in 2 arguments
    #by default there is an r for read open('C:\\Users\\Hasaan\\Documents\\Python\\test.txt', 'r')
    # add 'w' to write to file, this will overwrite itself 
    # add 'a' to append file
text="OMG\nthis is some text\nhave a good one\n"
with open('test.txt', 'w') as file:
    file.write(text)

text2="Im going to add a bit to the end, see ya!"
with open('test.txt', 'a') as file:
    file.write(text2)

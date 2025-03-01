# 35 Move a file or directory(folder)
    #import os module

text="OMG\nthis is some text\nhave a good one\n"
with open('move.txt', 'w') as file:
    file.write(text)

source="move.txt"
destination="C:\\Users\\Hasaan\\Documents\\Python\\movecomplete.txt"    #you ae moving move to your python folder and renaming movecomplete, remember you need to use double \\

try:
    if os.path.exists(destination):    #check if there is already a file there
        print("there is already a file here")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+ " was not found")
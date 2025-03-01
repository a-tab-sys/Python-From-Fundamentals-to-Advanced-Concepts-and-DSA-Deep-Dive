# 36 Delete File or directory
    #import os module
    # first you added a text file to project and called it delete(right click project in your workspace>new file)
    # you also created a folder called empty
    #you also created a folder called deletefolderwithfile and added a file to that folder
    #we will use try block for exception handling, not necessary

path="delete"       #file
try:
    os.remove(path)
    # or like this: os.remove('delete.txt')
except FileNotFoundError:
    print("File not found")
else:
    print(path + " was deleted")
    

#deleting empty folder requires another function, you cant use os.remove
path2="empty"            #empty folder
try:
    os.rmdir(path2)
except FileNotFoundError:
    print("File not found")
except PermissionError:                         #if you try to delete the empty folder, that requires another function
    print("you do not have permission to delete that")
else:
    print(path2 + " was deleted")

#to delete a folder with files you need import shutil module
path3="deletefolderwithfile"    #folder with file(s)
try:
    shutil.rmtree(path3)
except FileNotFoundError:
    print("File not found")
except PermissionError:                         #if you try to delete the empty folder, that requires another function
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete a directory with files using rmdir function")
else:
    print(path3 + " was deleted")
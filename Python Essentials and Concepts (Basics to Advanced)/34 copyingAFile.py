# 34 Copying a file
    #import the shutil module. there are others ways this is what we will use
    #this module has 3 basic functions
        # copyfile() - copys contents of a file
        # copy() - copyfile()+permission mode+destination can be a directory
        # copy2() - copy() + copies metadata (files creation and modification times)
    #all 3 above functions use the same 2 arguments

shutil.copyfile('test.txt', 'copy.txt') #2 arguments(source, destination) if its in same project, then add file name, it its elsewhere add the path
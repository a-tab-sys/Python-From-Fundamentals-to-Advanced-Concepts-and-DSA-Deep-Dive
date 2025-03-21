#37 Modules - a file containing python code. may contain functions, classes, etc.
            #used with modular progrmming, which is to seperate a program into parts
            #right clisk project>new>python file

            #if your working on a larger project, rather than having all the code in 1 file, you can have it in multiple files. each file will be referred to as a module

            #In Python, module names cannot contain spaces or special characters like numbers starting the name.

# in "37_modules_converter.py" file i will define 2 functions for converting lbs to kgs and kgs to lbs. i can take these 2 functions and put them in a seperate module called converters. then i will be able to import the converter module into any program that need the converter functions

import modules_converter_37     #to import entire module (file)
from modules_converter_37 import kg_to_lbs      #to import specific function from module. after you type import type ctrl+space to get a drop down of the function in the module


print(modules_converter_37.kg_to_lbs(70))   #if you import entire module, you need the module name to call specific functions

kg_to_lbs(100)    #dont need to add module name because you imported a specific function

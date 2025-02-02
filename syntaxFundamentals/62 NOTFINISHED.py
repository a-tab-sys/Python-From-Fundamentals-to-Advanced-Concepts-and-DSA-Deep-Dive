# 62 NOT WORKING RIGHT NOW, RETURN TO THIS LATER. UNFINISHED
# 62 if __name__=='__main__:'
        # y tho?
        # 1. Module can be run as a standalone program
        # 2. Module can be imported and  used by other modules

        # Python interpreter sets "special variables", one of which is __name__
        #then python will execute the code found in __main__

        #python files are also referred to as modules. by including this statement, it gives our modules
        #some flexibility, see 1 and 2 above
if __name__=='__main__':  #this statement checks to see if the user is runing this module as a standalone program, or its being imported from other modules
    pass

            #behind the scenes the python interpreter sets "special variables" one of which is __name__
            #python will assign the __name__ variable a value of '__main__' if its
            #the initial module being run

print(__name__) #since i am running this from this module/file, it will print __main__

import module_2
print(module_2.__name__)
# a package is a container for multiple modules, basically a directory or folder

# lets make a package called ecommerce

#you have to add a file with a specific naming convention into a directory. when pythons interpreter sees a file with this name in a directory (__init__) then it knows to treat this directory as a package

#3 ways you can call this. depending on how you call it will affect how you can use the functions within

import ecommerce.shipping   #import package.module

#call calc_shipping function
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping    #this makes it so that you dont have to write the package and module name everytime you want to call the calc_shipping function

calc_shipping()
calc_shipping()

from ecommerce import shipping

shipping.calc_shipping()
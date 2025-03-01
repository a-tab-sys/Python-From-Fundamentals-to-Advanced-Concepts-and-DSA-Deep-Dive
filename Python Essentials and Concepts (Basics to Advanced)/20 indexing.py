#20 Indexing
#   index operator [] = gives access to a sequences element (string, list, tuples)

name='bro code!'
if (name[0].islower()):     #checks is names first letter is caitalized, if it is not it capitalizes it
    name=name.capitalize()
print(name)

    #create a substring from first part of name, and make it uppercase
first_name=name[0:3].upper()    #or [:3]
print(first_name)

    #create substing of last name, and make it lowercase
last_name=name[4:]. lower()
print(last_name)

    #negative indexing
last_character=name[-1]
print(last_character)
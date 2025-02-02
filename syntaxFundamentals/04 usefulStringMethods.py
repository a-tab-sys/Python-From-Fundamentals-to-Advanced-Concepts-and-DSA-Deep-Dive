#04 Useful string methods
name="Bro Code"

    #prints length of string - would output 8
print(len(name))

    #finds where the first index of a certain character is, starts counting at 0...1...2
print(name.find("o"))

    #capitalize only the first letter of your entire string
print(name.capitalize())

    #makes your string all uppercase
print(name.upper())

    #makes your string all lowercase
print(name.lower())

    #returns true or false depending on whether the string is entirely composed of digits - would output false
print(name.isdigit())

    ##returns true or false depending on whether the string is entirely composed of alphabetical characters - would output false because we have a space in it
print(name.isalpha())

    ##Counts how many character are within our string - returns 2
print(name.count("o"))

    ##replaces a certain character, accepts 2 arguments("what to replace", "what to replae with")
print(name.replace("o", "a"))

    #display a string multiple times
print(name*3)
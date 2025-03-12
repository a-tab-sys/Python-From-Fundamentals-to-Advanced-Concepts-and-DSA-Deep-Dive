#04 Useful string methods
name="Bro Code"

    #prints length of string - would output 8
print(len(name))

    #finds where the first index of a certain character is, starts counting at 0...1...2
    #Returns: The index of the first occurrence of the substring, or -1 if not found.
print(name.find("o"))
# return name.find("o")

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


text = "apple banana apple cherry apple"
# Find the 1st occurrence
first_index = text.find("apple")   # 0
# Find the 2nd occurrence by starting after the first
second_index = text.find("apple", first_index + 1)  # 13
# Find the 3rd occurrence by starting after the second
third_index = text.find("apple", second_index + 1)  # 28
# In Python, property() is a built-in function that turns methods into something that looks like an attribute. It takes up to four arguments:

# property(fget, fset, fdel, doc)

# fget: The method to get the value (like getValue).
# fset: The method to set a new value (like setValue).
# fdel: The method to delete the value (like delValue).
# doc: (Optional) A docstring describing the property.

# You're telling Python:

# "If someone tries to access obj.value, call getValue.
# If they assign to obj.value, call setValue.
# If they delete obj.value, call delValue.

# Python program to explain property() function
# Alphabet class

class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value

    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value

    value = property(getValue, setValue, 
                     delValue, )


# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)

x.value = 'GfG'

del x.value

# Output
# Getting value
# GeeksforGeeks
# Setting value to GfG
# Deleting value
#05 Type Casting - convert a data type of a value to another data type
x=1         #int
y=2.0       #float
z="3"       #str

print(x)
print(y)
print(z)

print(int(y))
print(float(z))
print(str(z))

print(int(z)*3)
print(z*3)

# Convert binary string to integer
bstring="101"
print(int(bstring,2))
# The int() function is used to convert a string to an integer. The second argument (2) specifies the base of the input string. Since a is a binary string, specifying base 2 tells Python to interpret it as a binary number


# This formats integer into a binary string
# "{0:b}" is a format string where:
# 0 refers to the first argument inside .format().
# :b instructs Python to format the number as a binary string.
print("{0:b}".format(5))


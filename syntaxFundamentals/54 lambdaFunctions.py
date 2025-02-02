# 54 lambda functions
#       -function written in one line and use lambda keywrd
#       -accept any number of arguments, but only has one expression
#       (think of it as a shortcut)
#       (useful if needed for a short period of time, throw-away)
#lambda parameters:expression

def double(x):
    return x*2
print(double(5))

double = lambda x:x*2   # does the same as above using lambda function
multiply = lambda x, y:x*y
add=lambda x, y, z :x+y+z
full_name=lambda first_name, last_name: first_name+" "+last_name
age_check=lambda age: True if age>= 18 else False

print(double(5))
print(multiply(5, 6))
print(add(5, 6, 7))
print(age_check(18))
# 53 Higher order functions - a function that either
#                             1. accepts a function as an arguemnt 
#                                           or
#                             2. returns a function
#                             (in python, functions are also treated as objects)
    #1. accepts function as an arument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):        #passing in a function, could be loud or quiet, so we use arbitrary name func
    text=func("Hello")
    print(text)

hello(loud)     #call loud into hello function
hello(quiet)

    #2. retuns a function
def divisor(x):         #we passed in divisor(2) so x is 2
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))
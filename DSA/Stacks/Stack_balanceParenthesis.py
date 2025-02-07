# Balancing parenthesis: each opening symbol must have a corresponding closing symbol.

# (()()()()) - balanced
# (()((())())) - balanced
# ((((((()) - unbalanced
# ())) - unbalanced

# so how would we write an algorithm to read a string of parenthesis from left to right and decide whether the symbols are balanced. the most recent opening parenthesis must match the next closing parenthesis. 

# they match in reverse order: this is a clue that stacks can be used.


# its easy. lets start with an empty stack and begin processing string from left to right. 
# - if a symbol is an open parenthesis, push it in the stack, this is a signal that a coresponding closing symbol needs to appear later.
#  - if a symbol is a closing parenthesis, pop the stack


# if there is no opening symbol to match a closing symbol (too many closing symbols) - string is unbalanced
# as long as you can keep popping the stack to remove mathed opening symbols - string is balanced
# at the end of the string - an empty stack is a balanced one

from DSA.Stacks.Stack_implementEndBeginning import Stack
#from module.submodule import class
#from file import class

def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        # else if the curent character is )
        else:
            # If the stack is empty, it means there is no corresponding ( for this ), so the function returns False (unbalanced string)    
            if s.is_empty():
                return False
            # f the stack is not empty, pop the top item from the stack
            else:
                s.pop()

    # After the loop finishes, the function checks if the stack is empty
    return s.is_empty()


print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False
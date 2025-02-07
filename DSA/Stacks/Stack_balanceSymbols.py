# The parentheses checker can easily be extended to handle new types of symbols. Each opening symbol is pushed on the stack to wait for the matching closing symbol to appear later in the sequence. When a closing symbol does appear, the only difference is that we must check to be sure that it correctly matches the type of the opening symbol on top of the stack. If the two symbols do not match, the string is not balanced. 

# [ ] [ ] [ ] ( ) { } - balanced
# { { ( [ ] [ ] ) } ( ) } - balanced
# ( [ ) ] - unblanced
# ( ( ( ) ] ) ) - unbalanced

from DSA.Stacks.Stack_implementEndBeginning import Stack

def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        #if the symbol is not an opening symbol it must b a closing symbol
        else:
            # If the stack is empty, it means there's no opening symbol to match the current closing symbol, so the string is unbalanced, and the function returns False
            if s.is_empty():
                return False
            # else if the stack is not empty, the top symbol is popped from the stack using s.pop(), and the matches function is called to check if it matches the current closing symbol. If the symbols do not match, the string is unbalanced, and the function returns False
            else:
                if not matches(s.pop(), symbol):
                    return False

    return s.is_empty()

def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    # Uses the .index() method to find the position of sym_left in all_lefts and sym_right in all_rights. If the positions match, it means sym_left and sym_right are of the same type (e.g., ( matches )), and the function returns True
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))
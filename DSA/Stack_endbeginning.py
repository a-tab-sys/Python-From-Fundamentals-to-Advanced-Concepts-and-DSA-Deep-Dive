# assumes that the end of the list will hold the top element of the stack

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        """Python list (self._items) to store the stack's elements"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack. .append method adds item to the end of the list"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack. .pop method removes the last item"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack. -1 acceses the last element of the list"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)
    
s = Stack()

s.is_empty()
s.push(4)
print(s.peek())

s.push('dog')
print(s.peek())

s.push(True)
print(s.peek())

s.push (4.5)
print(s.peek())


print(s.size())

s.pop()
s.pop()

# s.pop().pop() #- Method chaining not working :/

print(s.peek())
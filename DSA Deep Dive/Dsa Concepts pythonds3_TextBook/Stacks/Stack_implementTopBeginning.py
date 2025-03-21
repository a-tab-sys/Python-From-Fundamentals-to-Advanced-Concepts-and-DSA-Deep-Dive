# implement the stack using a list where the top is at the beginning instead of at the end

class Stack:	    
    def __init__(self):	        
        self.items = []		    
    
    def is_empty(self):	        
        return self.items == []		    
    
    def push(self, item):	        
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s = Stack()
s.push("hello")
s.push("true")
print(s.pop())
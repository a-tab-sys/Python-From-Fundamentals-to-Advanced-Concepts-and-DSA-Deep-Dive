# SINGLY LINKED LIST

class SinglyNode:
    # constructor
    def __init__(self, val, next=None): #by default its none
        self.val=val
        self.next=next
    
    # string method so we can print node
    def __str__ (self):
        return str(self.val)
    
# The underscores in __str__ are part of Python's dunder methods (short for "double underscore" methods), also known as magic methods or special methods. These methods are predefined in Python and are used to enable special behavior for classes.
# The double underscores signify that this is a special method managed internally by Python.
# Python automatically looks for these methods during specific operations. For example:
# __init__() for object initialization
# __len__() for len() functionality
# __getitem__() for indexing
# __str__() for string conversion


Head=SinglyNode(2)
A=SinglyNode(3)
B=SinglyNode(4)
C=SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

# Traverse the list - O(n)
curr=Head
while curr:
    print(curr)
    curr = curr.next #once it reached C, C.next is None so while loop will end

# Display the list - O(n)
def display(head):
    curr=head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))
display(Head)

# Search for node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False
print(search(Head, 2))
print(search(Head, 7))

# DOUBLY LINKED LIST

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev

    def __str__(self):
        return str(self.val)


head=tail=DoublyNode(1)
print(tail)

# display function - O(n)
def display(head):
    curr=head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr=curr.next
    print(' <-> '.join(elements))

display(head)   

# Insert at the beginning - O(1)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev=new_node
    return new_node, tail  #returning head (head is the new node) and tail

head,tail=insert_at_beginning(head, tail, 3)

# Insert at the end - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node  #returning head and tail (tail is the new node)

head,tail=insert_at_beginning(head, tail, 3)
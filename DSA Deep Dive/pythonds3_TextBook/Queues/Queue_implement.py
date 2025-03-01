# Queues are build on top of lists and use the following list functionality:    
    # .pop()  #pop removes the last element
    # .insert(0, "addElement")    #insert lets you add an element to a certain index

# Need to decide which end of the list to use as the rear and which to use as the front.
# Here we will assume that the rear is at position 0 in the list. Will use the insert function to add new elements to the rear of the queue. 
# The pop operation can be used to remove the front element (the last element of the list)

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)
    
    def see_items(self):
        return self._items
    
    # you cant use loop to see all items in list, you will only see the front item because return will exit the function after the first iteration
    def see_front_item(self):
        for x in self._items:
            return(x)

q =Queue()

print(q.is_empty())

q.enqueue(4)
q.enqueue(False)
q.enqueue("dog")
q.enqueue(3.5)

print(q.is_empty())

print(q.see_items())

q.dequeue()

print(q.see_front_item())
print(q.see_items())
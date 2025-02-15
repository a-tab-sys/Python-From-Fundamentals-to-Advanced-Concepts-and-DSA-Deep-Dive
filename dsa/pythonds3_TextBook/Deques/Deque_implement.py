#Our implementation will assume that the rear of the deque is at position 0 in the list

#self._items is an instance variable that is initialized as an empty list ([]) in the constructor (__init__ method).
#The _ prefix (_items) is a convention in Python indicating that the variable is intended to be private and used only inside the class, but it is not enforced. You can still access or modify it directly if you need to
#Technically, you can directly access self._items from outside the class, but it's considered bad practice because:

#   It breaks encapsulation (hides the internal details of a class).
#   It can lead to bugs if someone modifies the list unexpectedly.

#Do not directly modify items: 
#deque._items.append(5)  # Directly modifying _items
#If your class defines methods (like add_front, add_rear, remove_front, etc.), it's better to use those rather than directly manipulating self._items. Encapsulation helps maintain control over how self._items is modified. Use helper methods to add/remove/modify items so you can add logic like validation, logging, or other functionality.

#Key Takeaways
#self._items can be treated like a normal list inside your class.
#It is better to create methods (like add_front, add_rear, etc.) to interact with self._items rather than directly accessing it from outside the class.
#Using methods helps encapsulate the behavior of the Deque, making it easier to maintain and modify later.

class Deque:
    """Deque implementation as a list"""

    def __init__(self):
        """Create new deque"""
        self._items = []

    def is_empty(self):
        """Check if the deque is empty"""
        return not bool(self._items)

    def add_front(self, item):
        """Add an item to the front of the deque(aka end of list). .append method adds item to the end of the list"""
        self._items.append(item)

    def add_rear(self, item):
        """Add an item to the rear of the deque (aka position 0 of list)"""
        self._items.insert(0, item)

    def remove_front(self):
        """Remove an item from the front of the deque (aka end of list)"""
        return self._items.pop()

    def remove_rear(self):
        """Remove an item from the rear of the deque (aka position 0 of list)"""
        return self._items.pop(0)

    def size(self):
        """Get the number of items in the deque"""
        return len(self._items)
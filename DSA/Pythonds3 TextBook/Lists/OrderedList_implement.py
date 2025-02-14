# As we consider the operations for the ordered list, we should note that the is_empty and size methods can be implemented the same as with unordered lists since they deal only with the number of nodes in the list without regard to the actual item values. Likewise, the remove method will work just fine since we still need to find the item and then link around the node to remove it. The two remaining methods, search and add, will require some modification.

from Node_Class import Node
class OrderedList:
    def __init__(self):
        self.head = None

    # unordered lists same approach would work with the ordered list and no changes are necessary if the item is in the list. however once the value in the node becomes greater than the item we are searching for, the search can stop and return False rather than moving forward throughout the entire list
    def search(self,item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next

        return False    
    
    # The most significant method modification will take place in add. Recall that for unordered lists, the add method could simply place a new node at the head of the list. It was the easiest point of access. Unfortunately, this will no longer work with ordered lists. It is now necessary that we discover the specific place where a new item belongs in the existing ordered list

    # Assume we have the ordered list consisting of 17, 26, 54, 77, and 93 and we want to add the value 31. The add method must decide that the new item belongs between 26 and 54. Figure 17 shows the setup that we need. As we explained earlier, we need to traverse the linked list looking for the place where the new node will be added. We know we have found that place when either we run out of nodes (current becomes None) or the value of the current node becomes greater than the item we wish to add. In our example, seeing the value 54 causes us to stop.

    # As we saw with unordered lists, it is necessary to have an additional reference, again called previous, since current will not provide access to the node that must be modified. Listing 10 shows the complete add method. Lines 3–4 set up the two external references and lines 8–9 again allow previous to follow one node behind current every time through the iteration. The condition (line 7) allows the iteration to continue as long as there are more nodes and the value in the current node is not larger than the item. In either case, when the iteration fails, we have found the location for the new node.

    # The remainder of the method completes the two-step process shown in Figure 17. Once a new node has been created for the item, the only remaining question is whether the new node will be added at the beginning of the linked list or some place in the middle. Again, previous is None (line 11) can be used to provide the answer.
    def add(self, item):
        """Add a new node"""
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp
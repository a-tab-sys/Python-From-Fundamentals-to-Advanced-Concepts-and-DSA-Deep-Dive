# Implementing an unordered list or linked list.

#imagine a collection of iems, for instance a bunch of floating numbers in a cloud. it appears that the numbers are placed randomly. if we hae some imformation on each item,like the location of the next item, then we know the relative position of the item by following the link to the next item.

#we need to know where the first item is, this needs to be explicitly specified. this external reference is referred to as the head of the list. Once we know where the first item is, that can tell us where the second, third, forth item is.

#THE NODE CLASS
#the building block for the linked list is the node. each node object has 2 pieced of info: it must hold the list item itself (data field) and a reference to the next node

#THE UNORDEREDLIST CLASS
from Node_Class import Node
class UnorderedList:
    # the constructor. Note that each list object will maintain a single reference to the head of the list. the special reference None will again be used to state that the head of the list does not refer to anything. The head of the list refers to the first node which contains the first item of the list. In turn, that node holds a reference to the next node (the next item), and so on. It is very important to note that the list class itself does not contain any node objects. Instead it contains a single reference to only the first node in the linked structure.
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    # Recall that the linked list structure provides us with only one entry point, the head of the list. All of the other nodes can only be reached by accessing the first node and then following next links.  This means that the easiest place to add the new node is right at the head, or beginning, of the list. In other words, we will make the new item the first item of the list and the existing items will need to be linked to this new first item so that they follow.
    def add(self, item):
        temp = Node(item)           #creates a new node and places the item as its data
        temp.set_next(self.head)    #changes the next reference of the new node to refer to the old first node of the list
        self.head = temp            #modify the head of the list to refer to the new node
        # The order of the two steps described above is very important. What happens if the order of line 64 and line 65 is reversed? If the modification of the head of the list happens first, the result can be seen in Figure 8. Since the head was the only external reference to the list nodes, all of the original nodes are lost and can no longer be accessed.


    # The next methods that we will implement–size, search, and remove–are all based on a technique known as linked list traversal. Traversal refers to the process of systematically visiting each node. To do this we use an external reference that starts at the first node in the list. As we visit each node, we move the reference to the next node by “traversing” the next reference
    
    # To implement the size method, we need to traverse the linked list and keep a count of the number of nodes that occurred. Again, the ability to compare a reference to None is very useful.
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

    # Searching for a value in a linked list implementation of an unordered list also uses the traversal technique. As we visit each node in the linked list we will ask whether the data stored there matches the item we are looking for. In this case, however, we may not have to traverse all the way to the end of the list. In fact, if we do get to the end of the list, that means that the item we are looking for must not be present. Also, if we do find the item, there is no need to continue. As in the size method, the traversal is initialized to start at the head of the list (line 2). We continue to iterate over the list as long as there are more nodes to visit. The question in line 4 asks whether the data item is present in the current node. If so, we return True immediately.
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False
    


    # Listing 7 shows the complete remove method. Lines 2–3 assign initial values to the two references. Note that current starts out at the list head as in the other traversal examples. previous, however, is assumed to always travel one node behind current. For this reason, previous starts out with a value of None since there is no node before the head (see Figure 11).In lines 6–7 we ask whether the item stored in the current node is the item we wish to remove. If so, we break out of the loop. If we do not find the item, previous and current must both be moved one node ahead. Again, the order of these two statements is crucial. previous must first be moved one node ahead to the location of current. At that point, current can be moved. This process is often referred to as inchworming, as previous must catch up to current before current moves ahead. Figure 12 shows the movement of previous and current as they progress down the list looking for the node containing the value 17.

    # Once the searching step of the remove has been completed, we need to remove the node from the linked list. Figure 13 shows the link that must be modified. However, there is a special case that needs to be addressed. If the item to be removed happens to be the first item in the list, then current will reference the first node in the linked list. This also means that previous will be None. We said earlier that previous would be referring to the node whose next reference needs to be modified in order to complete the removal. In this case, it is not previous but rather the head of the list that needs to be changed (see Figure 14). Another special case occurs if the item is not in the list. In that case current is None evaluates to True and an error is raised.
    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

my_list = UnorderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))

my_list.add(100)
print(my_list.search(100))
print(my_list.size())

my_list.remove(54)
print(my_list.size())
my_list.remove(93)
print(my_list.size())
my_list.remove(31)
print(my_list.size())
print(my_list.search(93))

try:
    my_list.remove(27)
except ValueError as ve:
    print(ve)
# The remaining methods append, insert, index, and pop are left as exercises. Remember that each of these must take into account whether the change is taking place at the head of the list or someplace else. Also, insert, index, and pop require that we name the positions of the list. We will assume that position names are integers starting with 0.
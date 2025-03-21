# Hashsets

# in python you would make a set and give it a variable name
# overtime we would just add things into that set
s=set()
print(s)

# Add item into set - *O(1) on average
s.add(1)
s.add(2)
s.add(3)
print(s)

# Lookup item in set - *O(1) on average
if 1 in s:
    print(True)
if 4 not in s:
    print(True)

# Remove item from set - *O(1) on average
# s.remove(4)   #causes an error because there is no 4 to remove
s.remove(3)
print(s)

# if you had a long string with many characters and many duplicates
# and you needed to know if a character was in there and needed to know that multiple times in a row, so that you would need to keep looking up into the string, tht would be slow.
# instead you could make a set of that stirng and it would take O(S) time
# the point of a set is to have only unique things so if we want to check what characters are in the set we dont need to look through all the duplicate characters

string='aaaaaaaaaaaabbbbbbbbbccccccccceeeeeeeeee'
sett=set(string) # Set construction - O(S) - s is the length of the string

print(sett)

# Loop through set elements in a set - O(n)
# would not really need to do this
for x in s:
    print(x)

# Hashmaps - in python these are dictionaries
# you can hash lots of things
# the key could be lots of different things, for now we will make them strings
# values could be many things as well; lists, nested lists, intergers...etc
d={'greg':1, 'steve':2,'rob':3}
dd={'greg':[1, 2, 3]}
print(d)

# Add key:val pair to dictionary - O(1)
d['arsh']=4
print(d)

# Check presence of key in dictionary - O(1)
if 'greg' not in d:
    print(True)

# Check the value coresponding to a key in the dictionary - O(1)
# before doing this you should check presence of the key, bc you get a key error if that key does not exist
print(d['greg'])
# print(d['gre'])         #will throw a key error

# Loop over key:val pairs of the dictionary - O(n)
for key, val in d.items():
    print (f'key {key}: val {val}')

# SOME CLEVER HASHMAPS


# Defaultdict
from collections import defaultdict

# make a defaultdict - pass in what you want a a default
# if we pass type int - basically the default interger is value of 0

default=defaultdict(int)
# default=defaultdict(list)

# so if we do default at the key of 2, we havnt put any key:value pairs in the dictionary but if you ran below you get 0

default[2]
# NORMALLY when we check for a key that does not exist we get a 0, this makes it so that we get a default value associated with the key
print(default)


#Counter
# counts the elements of the thing youve given it
from collections import Counter

print(string)

# you could count the frequesncy of elements with a normal discitonary and also with a defeaultdictionary but this is very simple
counter=Counter(string)
print(counter)



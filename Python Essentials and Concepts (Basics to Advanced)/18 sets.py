#18 Sets - collections which is unordered, unindexed.  No duplicate values allowed
utensils={"fork", "spoon", "knife"}
dishes={"bowl", "plate", "cup", "knife"}

seen = set()        #creates an empty set

for x in utensils:
    print(x)        #because its unindexed and unordered, when you print the items, it is in random order
#                    also faster processing because of this

    #see what happens when you add duplicate values
utensils1={"fork", "spoon", "knife", "knife", "knife"}
for x in utensils1:
    print(x)            #knife is only shown once

    #when you type <set name>. you will get list of funcions
    #adds element
utensils.add("napkins")
for x in utensils:
    print(x) 
    #removes element
utensils.remove("fork")
for x in utensils:
    print(x) 
    #clears set
utensils.clear()
for x in utensils:
    print(x) 

    #add one set to the other using update method
    #adds all elements in dishes set to utensils set
utensils.update(dishes)
for x in utensils:
    print(x)

    #join 2 sets to create an entirely new set
dinner_table=utensils.union(dishes)     #or vice versa

    #compare similarities nd differences between elements of different sets
    #prints what utensils has that dishes does not
print(utensils.difference(dishes)) #or vice versa
    #prints what utensils has in common with dishes
print(utensils.intersection(dishes)) 
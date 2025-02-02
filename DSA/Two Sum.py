"""
#Question
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
#--------------------------------------------------------      
"""
#Initial Solution - WRONG

class Solution(object):
    def twoSum(self, nums, target):
        for x in nums:
            for i in nums:
                if nums[x] + nums[i] == target:
                    return ("["+str(nums[x])+","+(str(nums[i]))+"]")
                    break
"""
#--------------------------------------------------------
"""
#Learning for Solution 1

listString = ["grape", 'cherry', 'banana']
listInt = [2,3,4]

#To loop through this list
for x in listString:
    print(x)

for x in listInt:
    print(x)
        #in this case i does not refer to the index, but it is referring to each individual item
        # 2, 3, 4 or grape, cherry, banana
        #so you cant later do nums[x] because its not referring to an index but to an item



#To loop through the list items by referring to their index number
for i in range(len(listString)):
    print (listString[i])

for i in range(len(listInt)):
    print (listInt[i])

#len tell that there are 3 items, then the range gives index 0-2


#Another issue was that you returned the values them selves rather than the indices
#and you didnt consider that you cant use the same element twice in a solution


#You could also have used a while loop to loop through elements
while i < len(listInt):
  print(listInt[i])
  i = i + 1

"""
#------------------------------------------------------
"""
#Solution 1 
class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):  # Iterate over indices
            for i in range(len(nums)):  # Iterate over indices again
                if x != i and nums[x] + nums[i] == target:  # Avoid comparing the same index
                    return [x, i]  # Return the indices
        return []  # Return an empty list if no solution is found
"""        
        
#------------------------------------------------------
"""
#Learning for Solution 2
Hash tables are a type of data structure in which the address 
# or the index value of the data element is generated from a hash function. 
# That makes accessing the data faster as the index value behaves as a key for the data value. 
# In other words Hash table stores key-value pairs but the key is generated through a hashing function.


#in Python the inplementation of of hash tables are done with the dictionary data type
#dictionary has key and value pairs 


#The enumerate() function in Python is a built-in function that 
#simplifies the process of iterating over a sequence (like a list) 
# while also keeping track of the index of the current element.
#enumerate(iterable, start=0) 
#   iterable being the sequence(list, tuple, string) you anna iterate over
#   start is optional but its the starting index (default is 0)
# enumerate() returns an iterable object where each iteration yields a tuple containing:

#The index of the current item.
#The value of the current item.
#i is the index of the current element.
#num is the value of the current element.

#How it works:
nums = [2, 7, 11, 15]

# Using enumerate to get both index and value
for i, num in enumerate(nums):
    print(f"Index: {i}, Value: {num}")


#Why Use enumerate()?
#When iterating over a list, if you need both the index and the value of each element:
"""
#------------------------------------------------------
"""
#Solution 2 

class Solution(object):
    def twoSum(self, nums, target):
        # Create a hash map/dictionary to store the value and its index
        num_map = {}
        
        # Iterate through the array
        #enumerate need you to give it 2 variables: i holds the index, num holds the value
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the complement exists in the hash map
            if complement in num_map:
                return [num_map[complement], i]  # Return the indices
            
            # Otherwise, add the current number and its index to the hash map
            num_map[num] = i
        
        return []  # Return an empty list if no solution is found

"""
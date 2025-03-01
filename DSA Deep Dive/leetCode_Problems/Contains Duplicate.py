"""
Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

"""





"""
Solution 1 Theory
We will use a set here

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.




"""






"""
#Solution 1 

class Solution(object):
    def containsDuplicate(self, nums):
        
        #:type nums: List[int]
        #:rtype: bool
        
        # Use a set to track seen elements
        seen = set()            #creates empty set
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

"""





"""
Solution 2 Theory
This approach converts the list into a set (which removes duplicates) and compares its length to the original list.

"""





"""
#Solution 2
class Solution(object):
    def containsDuplicate(self, nums):
        
        #:type nums: List[int]
        #:rtype: bool
        
        return len(nums) != len(set(nums))
"""





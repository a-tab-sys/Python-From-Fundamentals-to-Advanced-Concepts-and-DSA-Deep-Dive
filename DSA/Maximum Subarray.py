"""
Problem
53. Maximum Subarray

Given an integer array nums, find the 
subarray with the largest sum, and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""





"""
Solution 1 Theory

The idea is to run two nested loops to iterate over all possible subarrays and find the maximum sum. The outer loop will mark the starting point of a subarray and inner loop will mark the ending point of the subarray.
"""



"""
Solution 1 - Brute force method

# Python Program to find the maximum subarray sum using nested loops

# Function to find the sum of subarray with maximum sum

class Solution(object):
    def maxSubArray(self, nums):
        
        #:type nums: List[int]
        #:rtype: int
        
        res = arr[0]                #initialized to the arrays first element. it will store the largest sum found so far
  
    # Outer loop for starting point of subarray
    for i in range(len(arr)):       #outer loop iterates through all possible starting points of subarrays
        currSum = 0                 #for each starting point currSum=0
      
        # Inner loop for ending point of subarray
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]     #inner loop calculates the sum of the subarray starting at i and ending at j. Each iteration adds the element arr[j] to currSum, incrementally building the sum of the subarray.
          
            # Update res if currSum is greater than res
            res = max(res, currSum)     #After calculating currSum for the current subarray, res is updated to the maximum of its current value and currSum.
          
    return res              #Once all possible subarrays have been evaluated, res contains the maximum sum and is returned.


"""




"""
Solution 2 thoery - Kadane's Algorithm




"""






"""
Solution 2


class Solution(object):
    def maxSubArray(self, nums):
        
        #:rtype: int
        #:type nums: List[int]
        
        # Initialize variables
        max_sum = float('-inf')  # Smallest possible value to start
        current_sum = 0
        
        for num in nums:
            current_sum += num  # Add current number to the current sum
            max_sum = max(max_sum, current_sum)  # Update max sum if needed
            if current_sum < 0:  # Reset current sum if it goes negative
                current_sum = 0
        
        return max_sum


"""












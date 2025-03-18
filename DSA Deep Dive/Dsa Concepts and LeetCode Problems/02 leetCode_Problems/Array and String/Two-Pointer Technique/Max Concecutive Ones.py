# SOLUTION
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Find the maximum till now.
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 0
        return max(max_count, count)

# ONE-LINER SOLUTION
def findMaxConsecutiveOnes(self, nums):
  return max(map(len, ''.join(map(str, nums)).split('0')))






# MAP FUNCTION
# ex.
# map(function, iterable)
# The .map() function in Python is used for applying a function to each item in an iterable, like a list or tuple. It's a powerful tool for functional programming
# A map object (an iterator), which can be converted to a list, tuple, etc., using list() or tuple().

# MAP AND LEN FUNCTION - COMBINED USE
# ex.
# map(len, ['11', '111'])
# applies the len() function to each element in the list, returning their lengths.

# LIST FUNCTION
# ex.
# print(list(map(str, nums)))
# is used to convert the result of map() into a list.

# JOIN FUNCTION
# ex.
# ''.join(['1', '1', '0', '1', '1', '1'])
# used to join elements of an iterable (like a list, tuple, or set) into a single string. It’s a powerful and efficient way to concatenate multiple strings.
# SPLIT FUNCTION
# ex. 
# '110111'.split('0')
# splits the string at every '0', returning a list of consecutive '1' sequences.




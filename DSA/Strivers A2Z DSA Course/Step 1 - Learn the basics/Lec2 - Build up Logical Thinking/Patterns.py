# Patterns - Require nested loops - 4 rules
# (1) outer loop is for the rows
# (2) inner loop is focus on the columns and connect them with rows
# (3) printing will occur inside inner loop
# (4) observe symmetry [optional]

# Pattern 1 - https://www.geeksforgeeks.org/problems/square-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_1
# * * *
# * * *
# * * *
# class Solution:
#     def printSquare(self, N):
#         for i in range(N):
#             for j in range(N):
#                 print("*", end=" ")
#             print("")

# Pattern 2 - https://www.geeksforgeeks.org/problems/right-triangle/1
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# class Solution:
#     def printTriangle(self, N):
#             for i in range(1, N+1):
#                 print("* " * i)       

# Pattern 3 - https://www.geeksforgeeks.org/problems/triangle-number/1
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5 
class Solution:
    def printTriangle(self, N):
            
        for i in range(1, N+1):
            for k in range (1, i+1):
                print(k, end=" ")                
            print("")

# Pattern 4 - https://www.geeksforgeeks.org/problems/triangle-number-1661428795/1
# 1
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5   
# class Solution:
#     def printTriangle(self, N):
#         # Code
#         for i in range(1, N+1):
#             for j in range (1, i+1):
#                 print (i, end=" ")
#             print("")

# Pattern 5 - https://www.geeksforgeeks.org/problems/triangle-pattern/1
# * * * * * *
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# class Solution:
#     def printTriangle(self, N):
#         # Code here
#         for i in range (N, 0, -1):
#             print("* "*i)

# Pattern 6 - https://www.geeksforgeeks.org/problems/triangle-number-1661489840/1
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2  
# 1 
# class Solution:
#     def printTriangle(self, N):
#         # Code here
#         for i in range (N, 0, -1):
#             for j in range (1, i+1):
#                 print(j, end=" ")
#             print("")

# Pattern 7 - https://www.geeksforgeeks.org/problems/triangle-pattern-1661492263/1
#     *
#    ***  
#   *****
#  *******
# *********
# class Solution:
#     def printTriangle(self, N):
#         # Code here
#         for i in range(N):
#             # Print leading spaces followed by stars
#             print(" " * (N - i - 1) + "*" * (2 * i + 1))
# class Solution:
#     def printTriangle(self, N):
#         for row in range(1, 1 + N):
#             for space in range(N - row):
#                 print(' ', end = '')
#             for asterisk in range(1, 2 * row):
#                 print('*', end = '')
#             print()

# Pattern 8 - https://www.geeksforgeeks.org/problems/triangle-pattern-1661493231/1
# *********
#  *******
#   *****
#    ***
#     *
# class Solution:
#     def printTriangle(self, N):
#         # Code here
#         for i in range(N, 0,-1):
#             for spcs in range(N-i):
#                 print(" ", end="")
#             for astersks in range(i*2-1):
#                 print("*", end="")
#             print("")    

# Pattern 9 - https://www.naukri.com/code360/problems/star-diamond_6573686?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
#  *
#  ***
# *****
# *****
#  ***
#   *
# def nStarDiamond(n: int) -> None:
#     for j in range(1, 1+n):
#         for topspc in range(n-j):
#             print(" ", end="")
#         for topastk in range(j*2-1):
#             print("*", end="")
#         print("")
    
#     for i in range (n, 0, -1):
#         for spcs in range(n-i):
#             print(" ", end="")
#         for astr in range(i*2-1):
#             print("*", end="")
#         print("")
#     pass

# Pattern 10 - https://www.naukri.com/code360/problems/rotated-triangle_6573688?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
# *
# **
# ***
# **
# *
# def nStarTriangle(n: int) -> None:
#     for i in range (1, n+1):
#         for start in range (i):
#             print("*", end="")
#         print("")
#     for j in range (n-1, 0, -1):
#         for starb in range (j):
#             print("*", end="")
#         print("")
#     pass

# Pattern 11 - https://www.naukri.com/code360/problems/binary-number-triangle_6581890?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 
# 0 1 0 1 0 1
# def nBinaryTriangle(n: int) -> None:
#     for i in range(1, n + 1):
#         start = 1 if i % 2 != 0 else 0  # Start with 1 for odd rows, 0 for even rows
#         for j in range(i):
#             print(start, end=" ")
#             start = 1 - start  # Toggle between 1 and 0
#         print()  # Move to the next line

#     pass

# Pattern 12 - https://www.naukri.com/code360/problems/number-crown_6581894?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
# 1                         1
# 1 2                     2 1
# 1 2 3                 3 2 1
# 1 2 3 4             4 3 2 1
# 1 2 3 4 5         5 4 3 2 1
# 1 2 3 4 5 6     6 5 4 3 2 1
# 1 2 3 4 5 6 7 7 6 5 4 3 2 1  
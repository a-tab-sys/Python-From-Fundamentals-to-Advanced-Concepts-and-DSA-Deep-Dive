# PRINTING SOMETHING N TIMES

# ONE WAY
# use a global variable - 
# count = 0
# def printNtimes():
#     global count
#     if count == 3:
#         return
#     print(count)
#     count += 1
#     printNtimes()
# printNtimes()

# ANOTHER BETTER WAY
# pass count as an argument to the function
# passing count as an argument, is more Pythonic and better practice for recursive functions
# def printNtimes(count=0):
#     if count == 3:
#         return        # This exits the function
#     print(count)
#     printNtimes(count + 1)
# printNtimes()


# PRINT NAME N TIMES
# Problem: Print your Name N times using recursion
# def printName(N, i=0):      #In Python, parameters with default values must come after parameters without default values.
#     if i == N:
#         return
#     print("name")
#     printName(N, i+1)
# printName(4)


# PRINT 1 TO N USING RECURSION
# Problem: Print from 1 to N using Recursion
# def print1toN (N, i=1):
#     if i>N:
#         return
#     print(i)
#     print1toN(N, i+1)
# print1toN(4)


# PRINT N TO 1 USING RECURSION
# Problem: Print from N to 1 using Recursion
# def printNto1 (N, i=None):
#     if i is None:
#         i=N
    
#     if i<1:
#         return
#     print(i)
#     printNto1(N, i-1)
# printNto1(4)


# SUM OF FIRST N NATURAL NUMBERS
# Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.
# Example 1:
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Example 2:
# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

# ONE WAY - USING LOOP
# def printnaturalnums(N):
#     sum=0
#     for j in range (1,N+1):
#         sum+=j
#     return sum
# print(printnaturalnums(5))

# ANOTHER WAY - USING RECURSION
# when you return in a recursive call:
# the base case returns the final answer, but the issue is that each function call needs to return the result up the call stack so that the original function call (the first one) receives and returns the correct final result.
# def printnaturalnums2(N, sum=0, i=0):
#     if i>N:
#         return sum
#     # print(sum)
#     return printnaturalnums2(N, sum+i, i+1)     #need return in this line
# print(printnaturalnums2(6))

# ANOTHER WAY - DONE IN ONE LINE
# print(sum(range(6)))  # Output: 15


# FACTORIAL OF A NUMBER: ITERATIVE AND RECURSIVE
# Problem Statement: Given a number X,  print its factorial.
# Example 1:
# Input: X = 5
# Output: 120
# Explanation: 5! = 5*4*3*2*1

# Example 2:
# Input: X = 3
# Output: 6
# Explanation: 3!=3*2*1

# ONE WAY - USING LOOP









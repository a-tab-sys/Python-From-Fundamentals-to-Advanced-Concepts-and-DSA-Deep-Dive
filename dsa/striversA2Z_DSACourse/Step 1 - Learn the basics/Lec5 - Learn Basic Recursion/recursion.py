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
# def printfactorial(X):
#     fact=1
#     for i in range (1, X+1):
#         fact*=i
#         # print(fact)
#     print(fact)
# printfactorial(5)

# ANOTHER WAY - USING RECURSION
# def printfactorial1(X, fact=1, i=1):
#     if i>X:
#         return fact
#     return(printfactorial1(X, fact*i, i+1))
# print(printfactorial1(3))

# ANOTHER WAY - USING RECURSION
# Definition of factorial: n!=n×(n−1)!
# def factorial(X):
#     if X == 0 or X == 1:
#         return 1  # Base case: factorial of 0 and 1 is 1
#     return X * factorial(X - 1)  # Recursive call
# print(factorial(3))  

# REVERSE AN ARRAY
# Problem Statement: You are given an array. The task is to reverse the array and print it. 

# ONE WAY - USING LOOP - Modifies original list
# def reversearray(arr):
#     revarr=[]
#     while arr:  # While the list is not empty
#         revarr.append(arr.pop())
#     return revarr
# arr = [1, 2, 3, 4, 5]
# print(reversearray(arr))

# ANOTHER WAY - USING SLICING - FASTEST METHOD
# arr = [1, 2, 3, 4, 5]
# reversed_arr = arr[::-1]  
# print(reversed_arr)  # Output: [5, 4, 3, 2, 1]

# ANOTHER WAY - REVERSE() - Modifies originl list
# arr = [1, 2, 3, 4, 5]
# arr.reverse()  
# print(arr)  # Output: [5, 4, 3, 2, 1]

# ANOTHER WAY - USING RECURSION
# def revarray(arr, revarr=[]):
#     if not arr:             #checks if list is empty, could also do: if len(arr) == 0:
#         return revarr
#     revarr.append(arr.pop())  # Move last element from arr to revarr
#     return revarray(arr, revarr)  # Recursive call    
# arr = [1, 2, 3, 4, 5]
# print(revarray(arr))


# CHECK IF A STRING IS A PALINDROME OR NOT
# Problem Statement: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.
# Example 1:
# Input: Str =  “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.

# Example 2:
# Input: Str = “TAKE U FORWARD”
# Output: Not Palindrome
# Explanation: String when reversed is not the same as string.

# ONE WAY
# def checkpalindrome(orig):
#     rev=orig[::-1]
#     if (rev==orig):
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
# checkpalindrome("frtrf")
# checkpalindrome("frtrff")

# ANOTHER WAY - USING RECURSION 
def checkpalindrome(i, text):
    if i>len(text)/2:
        return True
    if(text[i]!=text[len(text)-1-i]):
        return False
    return checkpalindrome(i+1, text)
print(checkpalindrome(0, "frtrf"))
print(checkpalindrome(0, "frtrff"))

# PRINT FIBONACCI SERIES UP TO NTH TERM
# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term
# Example 1:
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

# Example 2:
# Input: 6
# Output: 0 1 1 2 3 5 8
# Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)










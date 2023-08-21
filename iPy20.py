""" Q.20. Given a positive integer n, find the pivot integer x such that:
The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. 
It is guaranteed that there will be at most one pivot index for the given input.
Example 1:
Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:
Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:
Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist. """

# Q20 Solution
import math

def pivotInteger(n: int):
        A = n*(n+1)//2
        for x in range(n+1):
            B, C = x*(x-1)//2, x*(x+1)//2
            if A - B == C:
              return x
        return -1

def pivotInteger2(n: int):
        if (x:=math.isqrt(x2:=n*(n+1)//2))**2 == x2:
          return x
        else:
          return -1

def pivotInteger3(n: int):
    value=False
    sumi = 0
    data = []
    for i in range(1, n+1):
        sumi += i
        sumj = 0
        for j in range(i, n+1):
            sumj += j
        if sumi == sumj:
            a, value=i, True
    if value==True:
        return a
    else:
        return -1

print(pivotInteger(8))
print(pivotInteger2(8))
print(pivotInteger3(8))

print(pivotInteger(4))
print(pivotInteger2(4))
print(pivotInteger3(4))
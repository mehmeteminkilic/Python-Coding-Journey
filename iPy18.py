""" Q.18. Given a positive integer n, find the sum of all integers 
in the range [1, n] inclusive that are divisible by 3, 5, or 7.
Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
Example 1:
Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. 
The sum of these numbers is 21.
Example 2:
Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. 
The sum of these numbers is 40. """

# Q18 Solution

def sumOfMultiples(n: int):
        res = 0
        for i in range(3, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                res += i
        return res

def sumOfMultiples2(n: int):
    divisions = [3, 5, 7]
    sum = 0
    for i in range(1, n+1):
        for j in divisions:
            if i % j == 0:
                sum += i
    return sum

print(sumOfMultiples(7))
print(sumOfMultiples2(7))

print(sumOfMultiples(10))
print(sumOfMultiples2(10))
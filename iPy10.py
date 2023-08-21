""" Q.10. Given an integer number n, return the difference 
between the product of its digits and the sum of its digits.
Example:
Input: n = 234
Output: 15
Explanation: Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15 """

def subtractProductAndSum(n:int):
    s = [int(i) for i in str(n)]
    prod = 1
    for num in s:
        prod *= num
    _sum = sum(s)
    return prod - _sum

def subtractProductAndSum2(n:int):
    product = 1; sum = 0
    for i in str(n):
        product = product * int(i)
        sum = sum + int(i)
    return product - sum

print(subtractProductAndSum(234))
print(subtractProductAndSum2(234))
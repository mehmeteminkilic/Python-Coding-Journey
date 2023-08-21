""" Q.15. Balanced strings are those that have an equal quantity of 'L' and 'R' characters. 
Given a balanced string s, split it in the maximum amount of balanced strings. 
Return the maximum amount of split balanced strings.
Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'. """

# Q15 Solution
def balancedStringSplit(s:str):
    res = cnt = 0
    for c in s:
        cnt += 1 if c == 'L' else -1
        if cnt == 0:
            res += 1
    return res

import itertools
def balancedStringSplit2(s:str):
    return list(itertools.accumulate(1 if c == "R" else -1 for c in s)).count(0)

def balancedStringSplit3(s):
    return sum(s[:i].count('L') * 2 == i for i in range(len(s)))

def balancedStringSplit4(s:str):
    count_l, count_r, max_splits = 0, 0, 0
    for char in s:
        if char == 'L':
            count_l += 1
        else:
            count_r += 1
        if count_l == count_r:
            max_splits += 1
            count_l, count_r = 0, 0
    return max_splits


print(balancedStringSplit("RLRRLLRLRL"))
print(balancedStringSplit2("RLRRLLRLRL"))
print(balancedStringSplit3("RLRRLLRLRL"))
print(balancedStringSplit4("RLRRLLRLRL"))

print(balancedStringSplit("RLLLLRRRLR"))
print(balancedStringSplit2("RLLLLRRRLR"))
print(balancedStringSplit3("RLLLLRRRLR"))
print(balancedStringSplit4("RLLLLRRRLR"))
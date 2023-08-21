""" Q.9. Given a string s and an integer array indices of the same length. 
The string s will be shuffled such that the character 
at the ith position moves to indices[i] in the shuffled string. 
Return the shuffled string.
Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position. """

def restoreString(s: str, indices: list):
    dct = dict(zip(indices, s))
    res = ""
    for i in range(len(s)):
        res += dct[i]
    return res

def restoreString2(s: str, indices: list):
    return ''.join([v for (_,v) in sorted(zip(indices,s))])

def  restoreString3(s: str, indices: list):
    n = len(s)
    m = len(indices)
    if n == m:
        new_string = []
        shuffled_string = ""
        for i in range(n):
            new_string += " "
        for j in range(n):
            new_string[indices[j]] = s[j]
        for k in range(n):
            shuffled_string+=new_string[k]
        return shuffled_string
    else:
        return print("lengths of given string and indices are not matched")


print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(restoreString2(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(restoreString3(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))

print(restoreString(s = "abc", indices = [0,1,2]))
print(restoreString2(s = "abc", indices = [0,1,2]))
print(restoreString3(s = "abc", indices = [0,1,2]))

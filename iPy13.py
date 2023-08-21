""" Q.13. Given an array of integers nums. 
A pair (i,j) is called good if nums[i] == nums[j] and i < j. 
Return the number of good pairs.
Example:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed. """

# Q13 Solution
def numIdenticalPairs(nums: list):
    res = 0
    for i in range(len(nums)):
        a = [nums[i]==num for num in nums]
        b = a[i+1:]
        res += sum(b)
    return res

def numIdenticalPairs2(nums: list):
    res = 0
    for i in range(len(nums)):
        res += nums[:i].count(nums[i])
    return res


def numIdenticalPairs3(nums: list):
    pairs = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] == nums[j]:
                pairs.append([i, j])
    return len(pairs)

print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs2([1,2,3,1,1,3]))
print(numIdenticalPairs3([1,2,3,1,1,3]))
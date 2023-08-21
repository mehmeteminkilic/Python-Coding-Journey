""" Q.14. Given two arrays of integers nums and index. 
Your task is to create target array under the following rules: 
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index. 
Return the target array.It is guaranteed that the insertion operations will be valid.
Example:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation: nums index target 0 0 [0] 1 1 [0,1] 2 2 [0,1,2] 3 2 [0,1,3,2] 4 1 [0,4,1,3,2] """


# Q14 Solution
def createTargetArray(nums:list, iindex:list):
    res = list()
    for i in range(len(nums)):
        res.insert(iindex[i], nums[i])
    return  res


def createTargetArray2(nums:list, iindex:list):
    target = [] ## Initially target array is empty.
    n = len(nums); m = len(iindex)
    # print(target)
    if n == m:
        for i in range(n):
            number_to_append = nums[i]
            index_to_append = iindex[i]
            target.insert(index_to_append, number_to_append) 
        return target
    else:
        print("the insertion operations are not valid due to the length mismatch between given numbers and indexes")

print(createTargetArray(nums = [0,1,2,3,4], iindex = [0,1,2,2,1]))
print(createTargetArray2(nums = [0,1,2,3,4], iindex = [0,1,2,2,1]))

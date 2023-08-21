""" Q.7. Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]. 
Return the answer in an array.
Example:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it. 
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2). """


# Q7 Solution
def smallerNumbersThanCurrent(nums:list):
    n = len(nums)
    result = list()
    for i in range(n):
        count = sum(1 for num in nums if num<nums[i] and num != nums[i])
        result.append(count)
    return result

def smallerNumbersThanCurrent2(nums:list):
    return [sorted(nums).index(a) for a in nums]

def smallerNumbersThanCurrent3(nums:list):
    return [len(list(filter(lambda x: x < n, nums))) for n in nums]

def smallerNumbersThanCurrent4(nums:list):
    res = []
    for x in nums:
        res.append(sum(y < x for y in nums))
    return res

def smallerNumbersThanCurrent5(nums:list):
    n = len(nums)
    num_smaller = []
    for i in range(n):
        count = 0
        for j in range(n):
            if  nums[i] >  nums [j]:
                count += 1
            else:
                count = count
        num_smaller.append(count)
    return num_smaller

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent2([8,1,2,2,3]))
print(smallerNumbersThanCurrent3([8,1,2,2,3]))
print(smallerNumbersThanCurrent4([8,1,2,2,3]))
print(smallerNumbersThanCurrent5([8,1,2,2,3]))

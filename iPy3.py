""" Q.3. Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. 
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
Example:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7]. """

def shuffleArray(nums:list, n:int):
    x_list, y_list = nums[:n], nums[n:]
    shuffled = list()
    for i in range(n):
        shuffled.extend([x_list[i], y_list[i]])
    return shuffled

def shuffleArray2(nums:list, n:int):
    shuffled = list()
    for i in range(n):
        shuffled.extend([nums[i], nums[i+n]])
    return shuffled

def shuffleArray3(nums:list, n:int):
    return sum(([nums[i], nums[i+n]] for i in range(n)), [])

def shuffleArray4(iarray):
    n = int(len(iarray)/2.)
    iarray_left = []
    iarray_right = []
    i = 0
    for number in iarray:
        if i < n:
            iarray_left.append(number)
        else:
            iarray_right.append(number)
        i = i + 1
    numbers_merge = []
    for i in range(n):
        numbers_merge.append(iarray_left[i])
        numbers_merge.append(iarray_right[i])
    return numbers_merge

print(shuffleArray([2,5,1,3,4,7], 3))
print(shuffleArray2([2,5,1,3,4,7], 3))
print(shuffleArray3([2,5,1,3,4,7], 3))
print(shuffleArray4([2,5,1,3,4,7]))
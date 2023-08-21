"""
Question: Given an array of numbers. Define a running sum of the array as runningSum[i] = sum(nums[0], ..., nums[i]).
Write a function to calculate and return the running sum of the given "nums" array.
"""

"""Answer"""
def running_sum(numbers):
    total = 0
    running_sums = []
    for number in numbers:
        total += number
        running_sums.append(total)
    return running_sums

import itertools

def running_sum2(numbers):
    return list(itertools.accumulate(numbers))

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]

    print("Running Sum with Method-1:", running_sum(numbers))
    print("Running Sum with Method-2:", running_sum2(numbers))
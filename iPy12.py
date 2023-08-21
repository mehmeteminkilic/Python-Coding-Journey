""" Q.12. Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has. 
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.
Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- 
the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.
Example 2:
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy. """

# Q12 Solution
def kidsWithCandies(candies: list, extraCandies: int):
    max_candy = max(candies)
    res = list()
    for candy in candies:
        if (candy + extraCandies) >= max_candy:
            res.append(True)
        else:
            res.append(False)
    return res

def kidsWithCandies2(candies: list, extraCandies: int):
    dif = max(candies) - extraCandies
    return [candy >= dif for candy in candies]

def kidsWithCandies3(candies: list, extraCandies: int):
    will_greatest = []
    for candy in candies:
        more_candy = []
        more_candy = candy + extraCandies
        greatest_value = []
        for candy in candies:
            if more_candy < candy:
                greatest_value.append('No')
            else:
                greatest_value.append('Yes')
        if "No" not in greatest_value:
            will_greatest.append(True)
        elif "No" in greatest_value:
            will_greatest.append(False)
    return will_greatest


print(kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(kidsWithCandies2(candies = [2,3,5,1,3], extraCandies = 3))
print(kidsWithCandies3(candies = [2,3,5,1,3], extraCandies = 3))

print(kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(kidsWithCandies2(candies = [4,2,1,1,2], extraCandies = 1))
print(kidsWithCandies3(candies = [4,2,1,1,2], extraCandies = 1))
""" Q.6. You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0 """

# Q6 Solution
def numJewelsInStones(jewels: str, stones: str):
    count = 0
    for stone in stones:
        for jewel in jewels:
            if stone == jewel:
                count += 1
    return count

def numJewelsInStones2(jewels, stones):
    return sum(s in jewels for s in stones)

def numJewelsInStones3(jewels, stones):
    return sum(map(stones.count, jewels))

print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStones2(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStones3(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStones(jewels = "z", stones = "ZZ"))
print(numJewelsInStones2(jewels = "z", stones = "ZZ"))
print(numJewelsInStones3(jewels = "z", stones = "ZZ"))

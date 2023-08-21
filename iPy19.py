"""" Q.19. You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:
* The string words[i] is equal to the reversed string of words[j].
* 0 <= i < j < words.length.
Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.
Example 1:
Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: In this example, we can form 2 pair of strings in the following way:
- We pair the 0th string with the 2nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1st string with the 3rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.
Example 2:
Input: words = ["ab","ba","cc"]
Output: 1
Explanation: In this example, we can form 1 pair of strings in the following way:
- We pair the 0th string with the 1st string, as the reversed string of words[1] is "ab" and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.  """

# Q19 Solution

def maximumNumberOfStringPairs(words: list):
    c=0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i]==words[j][::-1]:
                c+=1
    return c

def maximumNumberOfStringPairs2(words: list):
    strings = set()
    ans = 0
    for w in words:
        if w in strings:
            ans += 1
        else:
            strings.add(w[::-1])
    return ans

def maximumNumberOfStringPairs3(words: list):
    sum = 0
    for i in range(len(words)):
        word = words[i]
        for j in range(len(words)):
            if i < j:
                if word == words[j][::-1]:
                    sum += 1
                else:
                    sum = sum
    return sum


print(maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))
print(maximumNumberOfStringPairs2(["cd","ac","dc","ca","zz"]))
print(maximumNumberOfStringPairs3(["cd","ac","dc","ca","zz"]))

print(maximumNumberOfStringPairs(["ab","ba","cc"]))
print(maximumNumberOfStringPairs2(["ab","ba","cc"]))
print(maximumNumberOfStringPairs3(["ab","ba","cc"]))
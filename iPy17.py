""" Q.17. Given two string arrays word1 and word2, return true if the two arrays represent the same string, 
and false otherwise. A string is represented by an array if the array elements concatenated 
in order forms the string.
Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation: word1 represents string "ab" + "c" -> "abc" word2 represents string "a" + "bc" -> "abc" The strings are the same, so return true.
Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false """

# Q17 Solution
def arrayStringsAreEqual(word1:list, word2:list):
    a = "".join([i for i in word1])
    b = "".join([i for i in word2])
    return (a==b)

def arrayStringsAreEqual2(word1:list, word2:list):
    return "".join(word1) == "".join(word2)

def arrayStringsAreEqual3(word1:list, word2:list):
    iword1 = ""
    iword2 = ""
    for data1 in word1: iword1 += data1
    for data2 in word2: iword2 += data2
    
    if iword1 == iword2:
        return True
    else:
       return False
    
print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(arrayStringsAreEqual2(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(arrayStringsAreEqual3(word1 = ["ab", "c"], word2 = ["a", "bc"]))

print(arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(arrayStringsAreEqual2(word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(arrayStringsAreEqual3(word1 = ["a", "cb"], word2 = ["ab", "c"]))

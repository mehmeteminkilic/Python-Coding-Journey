""" Q.5. You are given an array items, where each items[i] = [typei, colori, namei] 
describes the type, color, and name of the ith item. 
You are also given a rule represented by two strings, ruleKey and ruleValue.
The ith item is said to match the rule if one of the following is true:
ruleKey == "type" and ruleValue == typei. ruleKey == "color" and ruleValue == colori. 
ruleKey == "name" and ruleValue == namei. Return the number of items that match the given rule.
Example:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 
ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"]. """

def countMatches(items, ruleKey: str, ruleValue: str):
    if ruleKey == "type":
        index = 0
    elif ruleKey == "color":
        index = 1
    else:
        index = 2
    count = 0
    for item in items:
        value = item[index]
        if value == ruleValue:
            count += 1
    return count

def countMatches2(items, ruleKey: str, ruleValue: str):
    rule = {'type' : 0, 'color' : 1, 'name' : 2}
    return sum(1 for item in items if item[rule[ruleKey]] == ruleValue)

def countMatches3(items, ruleKey: str, ruleValue: str):
    sum = 0
    for item in items:
        if ruleKey == "type" and ruleValue == item[0]:
            sum = sum + 1
        elif ruleKey == "color" and ruleValue == item[1]:
            sum = sum + 1
        elif ruleKey == "name" and ruleValue == item[2]:
            sum = sum + 1
    return sum

print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
print(countMatches2([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
print(countMatches3([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
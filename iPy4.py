"""Q.4. You are given an m x n integer grid accounts 
where accounts[i][j] is the amount of money the ith customer has in the jth bank. 
Return the wealth that the richest customer has. 
A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

Example:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation: 1st customer has wealth = 1 + 2 + 3 = 6 
2nd customer has wealth = 3 + 2 + 1 = 6 
Both customers are considered the richest with a wealth of 6 each, so return 6."""

# Q4 Solution
def maximumwealth(accounts):
    max_wealth = 0
    for customer in accounts:
        customer_wealth = sum(customer)
        if customer_wealth > max_wealth:
            max_wealth = customer_wealth
    return max_wealth

def maximumwealth2(accounts):
    max_wealth = 0
    for customer in accounts:
        customer_wealth = 0
        for acc in customer:
            customer_wealth += acc
        if customer_wealth > max_wealth:
            max_wealth = customer_wealth
    return max_wealth

def maximumwealth3(accounts):
    return max(map(sum, accounts))

def maximumwealth4(accounts):
    return max(sum(a) for a in accounts)

def maximumwealth5(accounts):
    wealth = []
    for i in range(len(accounts)):
        sum_of_account = 0
        for money in accounts[i]:
            sum_of_account += money
        wealth.append(sum_of_account)
    return max(wealth)

print(maximumwealth([[1,2,3],[3,2,1]]))
print(maximumwealth2([[1,2,3],[3,2,1]]))
print(maximumwealth3([[1,2,3],[3,2,1]]))
print(maximumwealth4([[1,2,3],[3,2,1]]))
print(maximumwealth5([[1,2,3],[3,2,1]]))
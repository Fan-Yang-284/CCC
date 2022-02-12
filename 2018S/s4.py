#Balancing Trees
from math import floor
N = int(input())

half = N//2 
res = N-half # any subtree number above half will just have k subtrees each with weight 1, resolving to 1

#subtree numbers below half, including half, will not necessarily resolve to 1

dp = {1:1,2:1} #memo

def getTrees(weight): # takes in number of subtrees, weight
    if weight in dp:
        return dp[weight]
    half1 = weight//2
    ans = weight-half1
    for i in range(half1,1,-1):
        ans += getTrees(floor(weight/i))
    dp[weight] = ans
    return ans

for i in range(half,1,-1): # for each of the k possible number of subtrees, add to res
    weight = floor(N/i)
    if weight in dp:
        res+=dp[weight]
    else:
        temp = getTrees(weight)
        res+=temp # takes in a number of subtrees, weight
        dp[weight] = temp
print(res)


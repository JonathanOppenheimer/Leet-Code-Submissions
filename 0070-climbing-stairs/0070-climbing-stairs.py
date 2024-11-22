class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        
        return dp[n]



# OPT(i) = OPT(i - 2) + OPT(i - 1)
# the number of ways to get to staircase i 

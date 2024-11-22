class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n_c = len(cost)
        dp = [-1] * (n_c + 1)
    
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n_c + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n_c]

# OPT(i) = min( OPT(i-2), OPT(i-1)  )
# the minimum cost to get to step i 
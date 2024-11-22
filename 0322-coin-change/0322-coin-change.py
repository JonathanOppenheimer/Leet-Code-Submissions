from math import inf 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        min_coin = min(coins)
        coint_set = set(coins)
        if amount < min_coin:
            return -1
        
        dp = (amount + 1) * [None]
        for i in range(0, min_coin):
            dp[i] = 0
            
        for i in range(min_coin, amount + 1): 
            if i in coint_set:
                dp[i] = 1
                continue

            min_count = inf
            for coin in coins: 
                if i - coin >= 0 and dp[i - coin] != 0: 
                    min_count = min(dp[i - coin] + 1, min_count) 
            dp[i] = min_count 
        
        if dp[amount] == inf:
            return -1 
        else: 
            return dp[amount]    
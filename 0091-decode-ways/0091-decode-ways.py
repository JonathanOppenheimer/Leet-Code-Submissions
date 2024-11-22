class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0

        if "00" in s:
            return 0
            
        if len(s) == 1:
            return 1 

        indices = []
        for i, value in enumerate(s):
            if value == '0':
                indices.append(i)
        for i in indices:
            if s[i-1] == '1' or s[i-1] == '2': 
                continue
            else:
                return 0 

        n_s = len(s)
        dp = [0] * n_s
        dp[0] = 1
        dp[1] = 2 if (int(s[0:2]) <= 26 and int(s[1]) != 0) else 1

        for i in range(2, n_s): # i = 3 2101
            if (s[i-1] != '0' and int(s[i-1:i+1]) <= 26 and int(s[i]) != 0):
                dp[i] = dp[i-2] + dp[i-1]
            else: 
                if int(s[i]) == 0: 
                    dp[i] = dp[i-2]
                else: 
                    dp[i] = dp[i-1]
        
        print(dp)
        return dp[n_s-1]
        


# OPT(i) - the number of ways to decode a message up to character i 

# e.g. 2101 

# opt[1] = 1 // 2
# opt[2] = 2 // 21 |  2 1   21
# OPT[3] = 1 // 210 | 2 10
# opt[4] = 


# 2 10 1


# OPT(1) = 1
# OPT(2) = 2 if s[1:3] < 26 else = 1
# OPT(3) = { OPT(1) if s[2:4 + 1] < 26 } + OPT(2)
# OPT(4) = { OPT(2) if s[3:5 + 1] < 26 } + OPT(3)
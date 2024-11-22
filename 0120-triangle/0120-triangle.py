class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n_t = len(triangle)
        if n_t < 2:
            return triangle[0][0]
        dp = [[-1]] * n_t
        for i in range(n_t):
            dp[i] = [-1] * (i+1)
        
        # row, col 
        # i (row), index (j)
        dp[0][0] = triangle[0][0]
        dp[1][0] = dp[0][0] + triangle[1][0]
        dp[1][1] = dp[0][0] + triangle[1][1]

        for i in range(2, n_t):
            n_dpi = len(dp[i])
            for j in range(n_dpi):
                if j == 0: 
                    dp[i][j] =  triangle[i][j] + dp[i-1][j]
                elif j == n_dpi - 1:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
        
        print(dp)
        return min(dp[n_t - 1])


# opt(i, j) - the minimum cost to get to index j on row i 
# return min j for op(len(list), j)

#    -1
#   3  2
# -3  1 -1
# 

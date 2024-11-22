

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)  # row count
        n = len(grid[0])  # column count
        
        dp = {}
        def calcMaxMoves(row, col): 
            move_right = 0 
            move_down = 0 
            move_diagonal = 0 
            
            if (row, col) in dp:
                return dp[(row, col)]

            if row - 1 >= 0 and col + 1 < n and grid[row - 1][col + 1] > grid[row][col]: 
                # print(f"{position}->{(row + 1, col)}: {grid[row][col]} went up right")
                move_down += 1 + calcMaxMoves(row - 1, col + 1)
            if col + 1 < n and grid[row][col + 1] > grid[row][col]:
                # print(f"{position}->{(row, col + 1)}: {grid[row][col]} went right")
                move_right += 1 + calcMaxMoves(row, col + 1)
            if row + 1 < m and col + 1 < n and grid[row + 1][col + 1] > grid[row][col]: 
                # print(f"{position}->{(row + 1, col + 1)}: {grid[row][col]} went down right")
                move_diagonal += 1 + calcMaxMoves(row + 1, col + 1)

            moves = max(move_right, move_down, move_diagonal)
            dp[(row, col)] = moves
            return moves

        max_moves = 0
        for i in range(m):
            max_moves = max(max_moves, calcMaxMoves(i, 0))
        return max_moves


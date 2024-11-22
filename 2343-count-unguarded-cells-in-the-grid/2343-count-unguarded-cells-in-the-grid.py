from pprint import pprint

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        # m = row
        # n = col 

        # 0 unguarded
        # 1 guard 
        # 2 covered by guard 
        # 3 wall 

        zero_tiles = m * n

        # place guards 
        for guard in guards:
            row, col = guard[0], guard[1]
            grid[row][col] = 1
            zero_tiles -= 1

        # place walls 
        for wall in walls:
            row, col = wall[0], wall[1]
            grid[row][col] = 3
            zero_tiles -= 1
        
        pprint(grid)
        for guard in guards:
            row, col = guard[0], guard[1]

            # look down 
            y, x = row, col 
            y += 1
            while y < m: 
                if grid[y][x] == 1 or grid[y][x] == 3:
                    break

                if grid[y][x] == 0:
                    zero_tiles -= 1
                    grid[y][x] = 2
                y += 1

            # look up
            y, x = row, col 
            y -= 1
            while y >= 0: 
                if grid[y][x] == 1 or grid[y][x] == 3:
                    break
                if grid[y][x] == 0:
                    zero_tiles -= 1
                    grid[y][x] = 2
                y -= 1

            # look right 
            y, x = row, col 
            x += 1
            while x < n: 
                if grid[y][x] == 1 or grid[y][x] == 3:
                    break
                if grid[y][x] == 0:
                    zero_tiles -= 1
                    grid[y][x] = 2
                x += 1

            # look left
            y, x = row, col 
            x -= 1
            while x >= 0: 
                if grid[y][x] == 1 or grid[y][x] == 3:
                    break
                if grid[y][x] == 0:
                    zero_tiles -= 1
                    grid[y][x] = 2
                x -= 1
        pprint(grid)
        return zero_tiles 


# [[1, 3, 0, 2, 0, 0], 
#. [2, 1, 2, 2, 3, 0], 
#. [2, 2, 3, 1, 2, 2], 
#. [2, 2, 0, 2, 0, 0]]


# [[1, 3, 2, 2, 2, 2], 
#. [2, 1, 2, 2, 3, 2], 
#  [2, 2, 3, 1, 2, 2], 
#  [2, 2, 0, 2, 0, 0]]


        
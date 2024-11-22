import random
from pprint import pprint

class Solution:
    def trap(self, height: List[int]) -> int:  
        n_height = len(height)

        l_tallest = [0] * n_height
        r_tallest = [0] * n_height

        tallest = 0
        for i in range(n_height):
            l_tallest[i] = tallest
            tallest = max(tallest, height[i])
        tallest = 0 
        for i in range(n_height - 1, -1, -1):
            r_tallest[i] = tallest
            tallest = max(tallest, height[i])
        
        # print(height)
        # print("***")
        # print(l_tallest)
        # print(r_tallest)

        water_collected = 0
        for i in range(n_height):
            l_t = l_tallest[i]
            r_t = r_tallest[i]
            h = height[i] 

            if l_t > h and r_t > h:
                water_collected += min(l_t, r_t) - h

        return water_collected

        #############################################################

        # max_elevation = max(height)
        # len_h = len(height)
        
        # b_l = (0, 0) # x, y 
        # b_r = (0, len_h)
        # t_l = (0, max_elevation)
        # t_r = (0, len_h)

        # board = [[0] * len_h for i in range(max_elevation)]

        # # row, col 
        # for col in range(len_h):
        #     cur_height = height[col]
        #     for row in range(max_elevation - cur_height, max_elevation):
        #         board[row][col] = 1

        # water_sum = 0
        # for row in range(max_elevation):
        #     water_counted_confirmed = 0
        #     water_counted = 0 
        #     counting = False 
        #     for col in range(len_h):
        #         if board[row][col] == 1:
        #             if counting:
        #                 counting = False
        #                 water_counted_confirmed += water_counted
        #                 water_counted = 0
        #             if not counting:
        #                 counting = True 
        #             continue 
                
        #         if counting:
        #             water_counted += 1                
        #     water_sum += water_counted_confirmed
               
        # return water_sum
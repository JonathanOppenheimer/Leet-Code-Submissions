import math

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_s = str(bin(start))[2:]
        goal_s = str(bin(goal))[2:]
        to_pad = abs(len(start_s) - len(goal_s))
        
        if len(start_s) - len(goal_s) > 0:
            goal_s = to_pad * '0' + goal_s
        else: 
            start_s = to_pad * '0' + start_s
            
        print(start_s)
        print(goal_s)
        
        flips = 0
        for i in range(len(start_s)):
            if start_s[i] != goal_s[i]:
                flips += 1 
        
        return flips
    

    

from collections import deque 

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        i = 0

        tot_r = 0 
        tot_d = 0

        for i in range(len(senate)):
            senator = senate[i]
            q.append(senator)
            if senator == 'R':
                tot_r += 1 
            else:
                tot_d += 1 

        to_ban_r_count = 0
        to_ban_d_count = 0

        num_r_banned = 0
        num_d_banned = 0 

        while True: # assume rationally that each senator bans the next senator 
            active_senator = q.popleft()        
            if active_senator == 'R':
                if to_ban_r_count > 0:
                    to_ban_r_count -= 1
                    num_r_banned += 1 
                    continue
                to_ban_d_count += 1
            else: 
                if to_ban_d_count > 0:
                    to_ban_d_count -= 1
                    num_d_banned += 1 
                    continue
                to_ban_r_count += 1

            q.append(active_senator)

            if num_r_banned == tot_r:
                return "Dire"
            
            if num_d_banned == tot_d: 
                return "Radiant"

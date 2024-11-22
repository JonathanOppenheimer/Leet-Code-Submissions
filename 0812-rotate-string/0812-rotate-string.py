class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        len_s = len(s)
        len_goal = len(goal)

        if len_s != len_goal:
            return False 

        successful_compares = 0
        shifts = 0 
        index = 0
        shift_index = 0
        while True:
            if shifts == len_s:
                return False
            
            if successful_compares == len_s:
                return True

            if s[(shifts + shift_index) % len_s] == goal[index]:
                successful_compares += 1
                index += 1 
                shift_index += 1 
            else:
                successful_compares = 0 
                index = 0
                shift_index = 0
                shifts += 1
            


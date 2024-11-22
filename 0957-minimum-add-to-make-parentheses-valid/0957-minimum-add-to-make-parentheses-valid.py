class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l_count = 0 # (
        r_count = 0 # ) 
        for c in s: 
            if c == '(':
                l_count += 1
            
            if c == ')':
                if l_count > 0:
                    l_count -= 1 
                else: 
                    r_count += 1 
        
        return l_count + r_count  
        
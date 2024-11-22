class Solution:
    def minLength(self, s: str) -> int:
        changed = True

        while changed:
            changed = False
            try:
                index = s.index("AB")
                s = s[:index] + s[index+2:]
                changed = True
            except: 
                pass

            try:
                index = s.index("CD")
                s = s[:index] + s[index+2:]
                changed = True
            except: 
                pass

        return(len(s))

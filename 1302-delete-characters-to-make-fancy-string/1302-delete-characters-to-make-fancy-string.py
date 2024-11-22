class Solution:
    def makeFancyString(self, s: str) -> str:
        last_char = ""
        count = 0
        new_string = ""
        deleted = 0 

        for char in s: 
            if char == last_char and count == 2:
                deleted += 1 
            else: 
                if char != last_char:
                    count = 0 
                last_char = char 
                count += 1
                new_string += char
                
        return new_string 


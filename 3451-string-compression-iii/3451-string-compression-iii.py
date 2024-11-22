class Solution:
    def compressedString(self, word: str) -> str:
        n_word = len(word)
        
        comp = ""
        
        count = 0 
        char = ""
        word_pos = 0
        while word_pos < n_word: 
            if count == 9:
                comp += "9" + char
                char = ""
                count = 0
            elif char == "":
                char = word[word_pos]
                count += 1 
                word_pos += 1 
            elif char != word[word_pos]:
                comp += str(count) + char
                char = ""
                count = 0
            else: # char == word[word_pos]:
                count += 1 
                word_pos += 1 
      
        comp += str(count) + char
        return comp
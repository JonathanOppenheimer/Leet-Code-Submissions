class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split(" ")
        arr.reverse()
        ans = ""
        for word in arr:
            if word != "":
                word = word
                ans += word + " "

        return ans.strip()
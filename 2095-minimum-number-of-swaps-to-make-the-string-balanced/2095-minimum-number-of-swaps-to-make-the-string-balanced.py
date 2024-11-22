class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        for char in s:
            if len(stack) != 0 and char == ']':
                if stack[-1] == '[':
                    stack.pop()
            else:
                stack.append(char)

        return int(len(stack)/2)
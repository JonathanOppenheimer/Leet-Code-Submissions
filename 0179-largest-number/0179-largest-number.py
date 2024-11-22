from functools import cmp_to_key

# want 34 > 3 > 30

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # return 1 if less than, -1 if greater than, 0 if same
        def lenSort(a, b):
            a = str(a) + str(b)
            b = str(b) + str(a)

            for i in range(len(a)):
                if int(a[i] == b[i]): 
                    continue 
                else:
                    return (1 if a[i] < b[i] else -1)
            return 0
            

        nums = sorted(nums, key=cmp_to_key(lenSort))
        print(nums)

        answer = ""
        for num in nums:
            answer += str(num)
    
        i = 0
        while i < len(answer) and answer[i] == "0" :
            i += 1
        
        if answer[i:] == "":
            return "0"
        return answer[i:]


        return answer
        
        

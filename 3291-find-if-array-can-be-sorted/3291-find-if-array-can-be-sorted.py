class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countSetBits(num):
            count = 0
            while num != 0:
                if num & 1:
                    count += 1
                num = num >> 1
            return count 

        nums_n = len(nums)
        
        for i in range(nums_n): 
            for j in range(nums_n - 1):
                num1 = nums[j]
                num2 = nums[j + 1]
                
                if num1 < num2:
                    continue
                else: 
                    if countSetBits(num1) == countSetBits(num2):
                        nums[j] = num2
                        nums[j + 1] = num1
                    else:
                        return False

        return True
    
        



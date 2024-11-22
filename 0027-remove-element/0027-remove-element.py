class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_n = len(nums)
        k = 0
        for i in range(len_n):
            num = nums[i]
            if num != val:
                nums[k] = num
                k += 1        
        return k
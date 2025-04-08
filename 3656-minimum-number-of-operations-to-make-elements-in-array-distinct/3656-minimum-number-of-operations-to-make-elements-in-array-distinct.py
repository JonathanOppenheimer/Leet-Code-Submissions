from collections import defaultdict 
from math import ceil 
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        n = len(nums)
        index = -1
        for i in range(n - 1, -1, -1):
            num = nums[i]
            counts[num] += 1 
            count = counts[num]
            if count > 1:
                index = i
                break
    
        return(ceil((index + 1)/3))

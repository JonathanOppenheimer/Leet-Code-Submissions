from collections import defaultdict 
from math import comb, perm

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        tuple_count = defaultdict(int)

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                ab = nums[i] * nums[j]
                tuple_count[ab] += 1
                
        running_sum = 0
        for half_tuple in tuple_count:
            lc = tuple_count[half_tuple]
            if lc > 1:
                running_sum += comb(lc, 2) * 8
        
        return running_sum


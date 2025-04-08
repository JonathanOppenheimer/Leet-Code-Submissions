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

        print("index: " + str(index))
        return(ceil((index + 1)/3))

        # if max(counts) == 1:
        #     return 0
        
        # cur_index = 0
        # n = len(nums)

        # print(counts)
        # while cur_index < n:
        #     num = nums[cur_index]
        #     print(num)
        #     if counts[num] == 1:
        #         cur_index += 1 
        #         continue 
        #     else: 
        #         removals += 1
        #         counts[num] -= 1
        #         if cur_index + 1 < n: counts[nums[cur_index + 1]] -= 1
        #         if cur_index + 2 < n: counts[nums[cur_index + 2]] -= 1
        #         cur_index += 3 

        # return removals 


 

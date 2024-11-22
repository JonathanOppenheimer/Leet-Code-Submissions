from collections import defaultdict 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        saved = defaultdict(int)
        
        for i in range(len(nums)):
            num = nums[i]
            if num not in saved: 
                saved[num] = i
            else: 
                if abs(i - saved[num]) <= k:
                    return True
                saved[num] = i
        return False 
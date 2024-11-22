from collections import deque

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        len_n = len(nums)
        num_set = set()
        max_sum = 0 
        cur_sum = 0 
        added_q = deque()

        for i in range(len_n):
            if len(num_set) == k:
                to_remove = added_q.popleft()
                num_set.remove(to_remove)
                cur_sum -= to_remove

            num = nums[i]
            if num in num_set: 
                to_remove = added_q.popleft()
                num_set.remove(to_remove)
                cur_sum -= to_remove
                while to_remove != num:
                    to_remove = added_q.popleft()
                    num_set.remove(to_remove)
                    cur_sum -= to_remove
            
            num_set.add(num)
            added_q.append(num) 
            cur_sum += num

            if len(num_set) == k:
                max_sum = max(max_sum, cur_sum)
    
        if len(num_set) == k:
            max_sum = max(max_sum, cur_sum)
        
        return max_sum 

            




            
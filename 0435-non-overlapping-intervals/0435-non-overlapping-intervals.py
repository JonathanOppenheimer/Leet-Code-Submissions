class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # maximize NON-OVERLAPPING INTERVALS

        #         0  1
        # last :  [1, 2]
        # cur  :  [2, 3]
        
        intervals_n = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[1])
  
        last_interval = intervals[0]
        discard = 0 
        for i in range(1, intervals_n):
            interval = intervals[i]
            if interval[0] < last_interval[1]: 
                discard += 1 
            else: 
                last_interval = interval

        return discard

      
       
 

    
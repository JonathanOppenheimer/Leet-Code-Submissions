class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = len(nums) -1 
        sub_array = []

        changed = False 
        
        while(index > 0):
            # Set minimum and save index 
            sub_array.append((nums[index], index))
            
            # Check to see if in descending order 
            if nums[index] <= nums[index - 1]:
                index -= 1; 
            else:
                # Get min value tuple 
                sub_array.sort(key=lambda x: x[0])
                for i in range(len(sub_array)):
                    if(nums[index - 1] < sub_array[i][0]):
                        right_min_num = sub_array[i]
                        break

                temp = nums[index - 1]
                nums[index - 1] = right_min_num[0]
                nums[right_min_num[1]] = temp 
                
                # Need to now sort index -> end 
                nums[index:len(nums)] = sorted(nums[index:len(nums)])
                changed = True 
                break
        
        # Got through entire array without swaps, sort ascending
        if not changed: 
            nums[0:len(nums)] = sorted(nums[index:len(nums)])

        return nums 
    



            
        
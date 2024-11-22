class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(n)
        n1 = len(nums1)
        n2 = len(nums2)

        big_array = []
        i1 = 0
        i2 = 0

        while len(big_array) != n1 + n2:
            if i1 >= n1: 
                big_array.append(nums2[i2])
                i2 += 1
                continue 
            
            if i2 >= n2: 
                big_array.append(nums1[i1])
                i1 += 1
                continue 

            if nums1[i1] < nums2[i2]:
                big_array.append(nums1[i1])
                i1 += 1
            else: 
                big_array.append(nums2[i2])
                i2 += 1
            
        middle = len(big_array) // 2 

        if len(big_array) % 2 == 0: 
            return (big_array[middle - 1] + big_array[middle])/2
        else: 
            return big_array[middle]

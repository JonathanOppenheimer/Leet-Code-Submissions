class Solution {
    public int findGCD(int[] nums) {
        int greatestArrayItem = 0; 
        for(int i=0; i<nums.length; i++) {
            if(nums[i] > greatestArrayItem) {
                greatestArrayItem = nums[i];
            }
        }
        int smallestArrayItem = 1001; 
        for(int i=0; i<nums.length; i++) {
            if(nums[i] < smallestArrayItem) {
                smallestArrayItem = nums[i]; 
            }
        }
        int greatestGCD = 0; 
        for(int i=1; i<=greatestArrayItem; i++) {
            if(smallestArrayItem%i == 0 && greatestArrayItem%i == 0) {
                greatestGCD = i; 
            }
        }
        return greatestGCD;
    }
}
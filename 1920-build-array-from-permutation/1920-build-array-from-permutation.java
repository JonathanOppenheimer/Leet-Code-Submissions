class Solution {
    public int[] buildArray(int[] nums) {
        int[] permuted = new int[nums.length];
        for(int i=0; i<permuted.length; i++) {
            permuted[i] = nums[nums[i]]; 
        }
        return permuted; 
    }
}
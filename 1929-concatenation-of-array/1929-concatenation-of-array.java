class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] doubledNums = new int[nums.length * 2]; 
        for(int i=0; i<nums.length; i++) {
            doubledNums[i] = nums[i]; 
        }
        for(int i=nums.length; i<doubledNums.length; i++) {
            doubledNums[i] = nums[i - nums.length];
        }
        return doubledNums; 
    }
}
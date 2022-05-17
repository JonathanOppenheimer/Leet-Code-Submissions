class Solution {
    public int[] decompressRLElist(int[] nums) {
        int arrayLength = 0;
        for(int i=0; i<nums.length; i+=2) {
            arrayLength += nums[i]; 
        }
        int[] decompressed = new int[arrayLength];
        int positionCount = 0;
        for(int i=0; i<nums.length; i+=2) {
            for(int j=0; j<nums[i]; j++) {
                decompressed[positionCount] = nums[i+1]; 
                positionCount++;
            }
        }
        return decompressed; 
    }
}
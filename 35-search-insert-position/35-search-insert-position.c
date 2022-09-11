

int searchInsert(int* nums, int numsSize, int target){
    for(int i=0; i<numsSize; i++) {
        printf("%d, %d\n", nums[i], target); 
        if(nums[i] > target) {
            return i;
        }
        if(nums[i] == target) {
            return i; 
        }
    }
    return numsSize; 
}
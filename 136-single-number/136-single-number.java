import java.util.ArrayList;

class Solution {
    public int singleNumber(int[] nums) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(int i=0; i<nums.length; i++) {
            arr.add(nums[i]); 
        }
        arr.sort(null);
        System.out.println(arr); 
        for(int i=0; i<nums.length; i++) {
           if(i != nums.length - 1) {
               int a = arr.get(i); 
               int b = arr.get(i+1);
               if(a != b) {
                   return a;
               } else {
                   i++; 
               }
           }
        }
        return arr.get(nums.length - 1); 
    }
}
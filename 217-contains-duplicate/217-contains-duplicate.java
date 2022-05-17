class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> everything = new HashMap<>();
        for(int i=0; i<nums.length; i++) {
            everything.put(i, nums[i]); 
        }
        Set<Object> duplicates = new HashSet<Object>(everything.values());
        System.out.println(duplicates); 
        if(duplicates.size() == everything.size()) {
            return false; 
        } else {
            return true; 
        }       
    }
}
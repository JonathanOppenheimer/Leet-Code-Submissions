class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandyCount = 0; 
        for(int i=0; i<candies.length; i++) {
            if(candies[i] > maxCandyCount) {
                maxCandyCount = candies[i]; 
            }
        }
        List<Boolean> moreCandy = new ArrayList<Boolean>(); 
        for(int i=0; i<candies.length; i++) {
            if(candies[i] + extraCandies >= maxCandyCount) {
                moreCandy.add(true);
            } else {
                moreCandy.add(false); 
            }
        }
        return moreCandy; 
    }
}
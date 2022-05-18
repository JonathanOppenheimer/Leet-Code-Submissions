class Solution {
    public int subtractProductAndSum(int n) {
        String number = Integer.toString(n);
        int sum = Character.getNumericValue(number.charAt(0));
        int product = sum;
        for(int i=1; i<number.length(); i++) {
            int temp = Character.getNumericValue(number.charAt(i)); 
            sum += temp; 
            product *= temp;  
        }
        return product - sum; 
    }
}
class Solution {
    public boolean isPalindrome(int x) {
        String number = Integer.toString(x);
        System.out.println(number); 
        int digitCount = number.length() - 1;
        for(int i=0; i < (digitCount+1)/2; i++) {
            if(number.charAt(i) != number.charAt(digitCount - i)) {
                return false; 
            }
        } 
        return true; 
    }
}
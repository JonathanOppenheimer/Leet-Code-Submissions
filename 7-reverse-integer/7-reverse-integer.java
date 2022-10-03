class Solution {
    public int reverse(int x) {
        String to_return = ""; // Use to build the number to be returned 
        int multiplier = 1; // Whether the number is negative or not
        int temp = x; // What to pull the digits from 
        
        if(x < 0) {
            multiplier = -1;
            temp = temp * -1; 
            
        }
        
        while(temp>0) {
            int last_digit = temp%10; 
            if(!(last_digit == 0 && to_return == "")) {
                to_return = to_return + last_digit; 
            }
            temp = (int)Math.floor(temp/10);
        }
        
        if(to_return == "") {
            return 0; 
        }
        
        try {
            return (multiplier * Integer.parseInt(to_return)); 
        } catch(NumberFormatException e) {
            return 0;
        }
    
    }
}
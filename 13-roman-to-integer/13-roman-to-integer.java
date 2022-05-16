class Solution {
    public int romanToInt(String romanNumeral) {
        int sum = 0; 
        for(int i=0; i< romanNumeral.length(); i++) {
            // Checks for I and all its cases 
            if(romanNumeral.charAt(i) == 'I') {    
                if(i != romanNumeral.length() - 1) {
                    // I before V 
                    if(romanNumeral.charAt(i + 1) == 'V') {
                        sum = sum + 4; 
                        i++;
                    } 
                    // I before X 
                    else if (romanNumeral.charAt(i + 1) == 'X') {
                        sum = sum + 9;
                        i++; 
                    }  
                    // Solo I 
                    else {
                        sum = sum + 1; 
                    }
                } 
                // Terminal I 
                else {
                    sum = sum + 1; 
                }
            }
            // Checks for V 
            else if(romanNumeral.charAt(i) == 'V') {
                sum = sum + 5; 
            }
            // Checks for X and all its cases 
            else if(romanNumeral.charAt(i) == 'X') {    
                if(i != romanNumeral.length() - 1) {
                    // X before L
                    if(romanNumeral.charAt(i + 1) == 'L') {
                        sum = sum + 40; 
                        i++;
                    } 
                    // X before C 
                    else if (romanNumeral.charAt(i + 1) == 'C') {
                        sum = sum + 90;
                        i++; 
                    }  
                    // Solo X 
                    else {
                        sum = sum + 10; 
                    }
                } 
                // Terminal X
                else {
                    sum = sum + 10; 
                }
            } 
            // Checks for L 
            else if(romanNumeral.charAt(i) == 'L') {
                sum = sum + 50; 
            }
            // Checks for C and all its cases 
            else if(romanNumeral.charAt(i) == 'C') {    
                if(i != romanNumeral.length() - 1) {
                    // C before D
                    if(romanNumeral.charAt(i + 1) == 'D') {
                        sum = sum + 400; 
                        i++;
                    } 
                    // C before M 
                    else if (romanNumeral.charAt(i + 1) == 'M') {
                        sum = sum + 900;
                        i++; 
                    }  
                    // Solo C
                    else {
                        sum = sum + 100; 
                    }
                } 
                // Terminal C
                else {
                    sum = sum + 100; 
                }
            } 
            // Checks for D
            else if(romanNumeral.charAt(i) == 'D') {
                sum = sum + 500; 
            }
            // Checks for M
            else if(romanNumeral.charAt(i) == 'M') {
                sum = sum + 1000; 
            }
        }
        return sum; 
    }
}
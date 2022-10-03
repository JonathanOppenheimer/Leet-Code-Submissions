class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length() > haystack.length()) {
            return -1; 
        }   
        
        for(int i=0; i<haystack.length(); i++) {
            if(haystack.charAt(i) == needle.charAt(0)) {
                if(needle.length() == 1) {
                    return i; 
                }
                
                if(i + needle.length() - 1 > haystack.length() - 1) {
                    return -1; 
                }
                    
                boolean equal = true; 
                for(int j=i; (j-i)<needle.length(); j++) {
                    if(!(haystack.charAt(j) == needle.charAt(j-i))) {
                        equal = false; 
                        break; 
                    }
                }
                if(equal) {
                    
                    return i; 
                }
            }
        }
        return -1; 
    }
}
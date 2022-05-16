class Solution {
    public String longestCommonPrefix(String[] strs) {
        boolean stillMatching = true; 
        int runCount = 0; 
        StringBuilder builder = new StringBuilder("");
        try {
            builder.append(strs[0].charAt(0)); 
        } catch(Exception e) {
            return ""; 
        }
        
        while(stillMatching) {
            for(int i=0; i<strs.length; i++) {
                try {
                   if(strs[i].charAt(runCount) != builder.charAt(runCount)) {
                        stillMatching = false; 
                    } 
                } catch(Exception e) {
                    stillMatching = false; 
                    break; 
                }
                
            }
            if(stillMatching) {
                runCount++;
                try {
                    builder.append(strs[0].charAt(runCount)); 
                } catch(Exception e) {
                    return builder.toString(); 
                }
            } else {
                builder.deleteCharAt(runCount); 
                break; 
            }
        }
        return builder.toString(); 
    }
}
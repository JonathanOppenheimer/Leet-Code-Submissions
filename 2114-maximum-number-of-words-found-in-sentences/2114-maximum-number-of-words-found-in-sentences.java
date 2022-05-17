class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxWords = 0;
        for(int i=0; i<sentences.length; i++) {
            int wordCount = 1; 
            for(int j=0; j<sentences[i].length(); j++) {
                if(sentences[i].charAt(j) == ' ') {
                    wordCount++;
                }
            }
            if(wordCount > maxWords) {
                maxWords = wordCount;
            }
        }
        return maxWords; 
    }
}
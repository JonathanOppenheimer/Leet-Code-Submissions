class Solution {
    public String restoreString(String s, int[] indices) {
        StringBuilder unshuffled = new StringBuilder(s);
        for(int i=0; i<indices.length; i++) {
          unshuffled.setCharAt(indices[i], s.charAt(i)); 
        }
        return unshuffled.toString(); 
    }
}
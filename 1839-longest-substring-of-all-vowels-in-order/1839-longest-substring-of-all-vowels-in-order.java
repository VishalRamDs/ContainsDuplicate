class Solution {
    public int longestBeautifulSubstring(String word) {
        int vowelCount=1;
        int length=1;
        int maxLen=0;
        for(int i=1;i<word.length();i++){
            if(word.charAt(i)<word.charAt(i-1)){
                vowelCount=1;
                length=1;
            }
            else if(word.charAt(i)>word.charAt(i-1)){
                vowelCount++;
                length++;
            }
            else{
                length++;
            }
            if(vowelCount==5){
                maxLen=Math.max(maxLen,length);
            }
        }
        return maxLen;
    }
}
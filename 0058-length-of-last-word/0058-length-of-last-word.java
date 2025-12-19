class Solution {
    public int lengthOfLastWord(String s) {
        int length=0;
        int current=s.length()-1;

        while(current>=0 && s.charAt(current)==' '){
            current--;
        }
        while(current>=0 && s.charAt(current)!=' '){
            length++;
            current--;
        }
        return length;
    }
}
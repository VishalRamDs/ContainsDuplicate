class Solution {
    public boolean isPalindrome(int x) {
       if(x<0){
        return false;
       }
       String original=String.valueOf(x);
       String reverse=new StringBuilder(original).reverse().toString();
       return original.equals(reverse);
    }
}
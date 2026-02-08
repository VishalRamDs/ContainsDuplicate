import java.util.*;
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        long expected = (long) n * (n + 1) / 2; // use long to avoid overflow
        long actual = 0;
        for (int v : nums) actual += v;
        return (int) (expected - actual);
        
    }
}
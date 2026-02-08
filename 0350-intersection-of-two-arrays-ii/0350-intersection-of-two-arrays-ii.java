class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int i=0,j=0;
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        List<Integer>temp=new ArrayList<>();
        while(i<nums1.length && j<nums2.length){
            if(nums1[i]==nums2[j]){
                temp.add(nums1[i]);
                i++;
                j++;
            }
            else if(nums1[i]<nums2[j]){
                i++;
            }
            else{
                j++;
            }
        }

        int[] ans=new int[temp.size()];
        for(int k=0;k<temp.size();k++){
            ans[k]=temp.get(k);
        }
        return ans;
        
    }
}
class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        #using sum formula approach
        expect=n*(n+1)//2
        actual=sum(nums)
        return expect-actual
        
        
        
class Solution(object):
    def guessNumber(self, n):
        left=1
        right=n
        while left<=right:
            mid=(left+right)//2
            result=guess(mid)
            if result==-1:
                right=mid-1
            elif result==1:
                left=mid+1
            elif result==0:
                return mid


        
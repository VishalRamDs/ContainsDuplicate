class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        seen=set(nums)
        container=list()
        for num in range(1,n+1):
            if num not in seen:
                container.append(num)
        return container
        
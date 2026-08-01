class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        seen=set()
        container=list()
        for num in nums:
            if num in seen:
                 container.append(num)
            seen.add(num)
        for num in range(1,n+1):
            if num not in seen:
                container.append(num)
        return container
        
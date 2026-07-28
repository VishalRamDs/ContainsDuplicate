class Solution(object):
    def containsDuplicate(self, nums):
        Container={}
        for i,num in enumerate(nums):
            if num in Container:
                return True
            Container[num]=i
        return False

        
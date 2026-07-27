class Solution(object):
    def twoSum(self, nums, target):
       Container={}
       for i,num in enumerate(nums):
           Complement=target-num
           if Complement in Container:
               return [Container[Complement],i]
           Container[num]=i
       return []      
        
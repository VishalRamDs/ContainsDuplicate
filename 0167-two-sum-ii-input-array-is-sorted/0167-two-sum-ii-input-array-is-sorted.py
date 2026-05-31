class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while left < right:
            is_target = numbers[left] + numbers[right]
            if is_target==target:
                return [left+1,right+1]
            elif is_target<target:
                left+=1
            else:
                right-=1
            


        
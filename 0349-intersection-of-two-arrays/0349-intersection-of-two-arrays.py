class Solution(object):
    def intersection(self, nums1, nums2):
        seen=set()
        container=set()

        for num in nums1:
            if num not in seen:
                seen.add(num)
        for num in nums2:
            if num in seen:
                container.add(num)

        return list(container)
class Solution(object):
    def intersection(self, nums1, nums2):
        result=set()
        for i in nums1:
            if i in nums2:
                result.add(i)
        return list(result)

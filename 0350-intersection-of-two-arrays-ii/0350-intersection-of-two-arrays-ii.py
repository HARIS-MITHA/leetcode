class Solution(object):
    def intersect(self, nums1, nums2):
        freq = {}
        result = []
        for i in nums1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for j in nums2:
            if j in freq and freq[j] > 0:
                result.append(j)
                freq[j] -= 1
        return result
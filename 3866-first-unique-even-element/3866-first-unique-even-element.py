class Solution(object):
    def firstUniqueEven(self, nums):
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in nums:
            if i% 2 == 0 and freq[i] == 1:
                return i
        return -1
        
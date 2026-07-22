class Solution(object):
    def missingNumber(self, nums):
        numbers = set(nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in numbers:
                return i  
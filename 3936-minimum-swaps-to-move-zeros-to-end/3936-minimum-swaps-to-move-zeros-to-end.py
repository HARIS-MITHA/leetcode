class Solution(object):
    def minimumSwaps(self, nums):
        zero = nums.count(0)
        swaps = 0
        start = len(nums) - zero
        for i in range(start, len(nums)):
            if nums[i] != 0:
                swaps += 1
        return swaps
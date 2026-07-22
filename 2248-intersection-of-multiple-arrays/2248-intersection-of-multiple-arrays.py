class Solution(object):
    def intersection(self, nums):
        common=set(nums[0])
        for i in range(1,len(nums)):
            current=set(nums[i])
            common=common.intersection(current)
        return sorted(list(common))
         
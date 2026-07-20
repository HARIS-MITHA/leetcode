class Solution(object):
    def pivotIndex(self, nums):
        totalsum=sum(nums)
        sumleft=0
        sumright=totalsum
        for i in range(len(nums)):
            sumright-=nums[i]
            if sumleft==sumright:
                return i
            sumleft+=nums[i]
        return -1

        
class Solution(object):
    def moveZeroes(self, nums):
        result=[]
        for i in range(0,len(nums)):
            if nums[i]!=0:
                result.append(nums[i])
        while len(result) < len(nums):
            result.append(0)
        for i in range(len(nums)):
            nums[i] = result[i]
        
        
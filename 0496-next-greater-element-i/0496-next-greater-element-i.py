class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        nextgreater={}
        for num in nums2:
            while stack and num >stack[-1]:
                nextgreater[stack.pop()]=num
            stack.append(num)
        while stack:
            nextgreater[stack.pop()]=-1
        result=[]
        for num in nums1:
            result.append(nextgreater[num])
        return result
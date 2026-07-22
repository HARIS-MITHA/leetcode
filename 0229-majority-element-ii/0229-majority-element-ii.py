class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans=[]
        for j in freq:
            if freq[j]>len(nums)/3:
                ans.append(j)
        return ans
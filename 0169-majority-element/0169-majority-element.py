class Solution(object):
    def majorityElement(self, nums):
            freq={}
            for i in nums:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
            larg_freq=0
            answer=0
            for j in freq:
                if freq[j]>larg_freq:
                    larg_freq=freq[j]
                    answer=j
            return answer
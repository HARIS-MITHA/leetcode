class Solution(object):
    def digitFrequencyScore(self, n):
        freq={}
        for i in str(n):
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans=0
        for i in freq:
            ans+=int(i)*freq[i]
        return ans
        
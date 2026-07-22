class Solution(object):
    def uniqueOccurrences(self, arr):
            freq={}
            for i in arr:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
            return len(freq.values())==len(set(freq.values()))
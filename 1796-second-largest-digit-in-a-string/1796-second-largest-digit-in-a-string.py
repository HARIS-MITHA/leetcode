class Solution(object):
    def secondHighest(self, s):
        nums="0123456789"
        digits=[]
        for i in range(len(s)):
            if s[i] in nums:
                digits.append(int(s[i]))
        digits=set(digits)
        if len(digits)>0:
            digits.remove(max(digits))
            if len(digits)>0:
                return max(digits)
            else:
                return -1
        else:
            return -1
        
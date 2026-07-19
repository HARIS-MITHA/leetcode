class Solution(object):
    def validDigit(self, n, x):
        s=str(n)
        p=str(x)
        if s[0]!=p:
            if p in s:
                return True
        return False
        
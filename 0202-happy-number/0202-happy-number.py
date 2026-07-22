class Solution(object):
    def isHappy(self, n):
        seen=set()
        while True:
            if n in seen:    
                return False
            seen.add(n)
            sum=0
            while n>0:
                digit=n%10
                sum+=digit*digit
                n=n//10
            n=sum 
            if n==1:
                return True

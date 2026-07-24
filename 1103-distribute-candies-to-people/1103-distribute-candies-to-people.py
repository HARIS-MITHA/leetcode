class Solution(object):
    def distributeCandies(self, candies, num_people):
        result=[0]*num_people
        give=1
        i=0
        while candies>0:
            if candies>=give:
                result[i]+=give
                candies-=give
            else:
                result[i]+=candies
                candies=0
            give+=1
            i=(i+1)%num_people
        return result


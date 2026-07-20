class Solution(object):
    def duplicateZeros(self, arr):
        result=[]
        for i in range(len(arr)):
            if arr[i]==0:
                result.append(0)
                result.append(0)
            else:
                result.append((arr[i]))
        for i in range(len(arr)):
            arr[i]=result[i]
        
class Solution(object):
    def lengthOfLastWord(self, s):
        lst=s.split()
        word=lst[-1]
        return len(word)
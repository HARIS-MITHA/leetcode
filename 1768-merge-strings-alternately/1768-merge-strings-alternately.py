class Solution(object):
    def mergeAlternately(self, word1, word2):
        empty=""
        minimum_length=min(len(word1),len(word2))
        for i in range(0,minimum_length):
            empty+=word1[i]
            empty+=word2[i]
        empty+=word1[minimum_length:]
        empty+=word2[minimum_length:]
        return empty

        
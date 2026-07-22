class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        dict1= {}
        dict2= {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if p in dict1:
                if dict1[p] != w:
                    return False
            else:
                dict1[p] = w
            if w in dict2:
                if dict2[w] != p:
                    return False
            else:
                dict2[w]= p
        return True     
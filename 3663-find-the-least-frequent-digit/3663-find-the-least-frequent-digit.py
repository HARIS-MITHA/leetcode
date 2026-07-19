class Solution(object):
    def getLeastFrequentDigit(self, n):
        s = str(n)
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        minimum = min(freq.values())
        ans = 9
        for digit in freq:
            if freq[digit] == minimum:
                ans = min(ans, int(digit))
        return ans

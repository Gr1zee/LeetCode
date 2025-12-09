class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i1 = 0
        i2 = 0
        while i1 + i2 < len(word1) + len(word2):
            if i1 < len(word1):
                res += word1[i1]
                i1 += 1
            if i2 < len(word2):
                res += word2[i2]
                i2 += 1
        return res

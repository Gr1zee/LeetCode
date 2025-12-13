class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        win = s[0:k]
        vow = "aeiou"
        c = 0
        for b in win:
            if b in vow:
                c += 1
        result = c

        for i in range(k, len(s)):
            if s[i] in vow:
                c += 1
            if vow[i - k] in vow:
                c -= 1
            result = max(result, c)
        return result


s = Solution()
print(s.maxVowels("abciiidef", 3))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        Alph = "qwertyuiopasdfghjklzxcvbnm"
        s = s.lower()
        ls = [x for x in list(s) if x in Alph]
        p1 = 0
        p2 = len(ls)-1
        for i in range(0, len(ls)//2-1):
            if ls[p1] != ls[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
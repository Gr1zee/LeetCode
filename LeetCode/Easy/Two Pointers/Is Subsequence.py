class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p_s = 0
        p_t = 0
        if len(s) == 0:
            return True
        if s == t:
            return True
        while p_t < len(t):
            if len(s) > 0 and t[p_t] == s[p_s]:
                p_s += 1
            p_t += 1
            if p_s == len(s) and p_s != 0:
                return True
        return False

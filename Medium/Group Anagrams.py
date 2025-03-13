class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        preobr = {}
        for i in range(len(strs)):
            s = "".join(sorted(list(strs[i])))
            if s in preobr:
                preobr[s] += [strs[i]]
            else:
                preobr[s] = [strs[i]]
        for k in preobr:
            res.append(preobr[k])
        return res

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


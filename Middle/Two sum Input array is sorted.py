class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            s = numbers[p1] + numbers[p2]
            if s == target:
                return [p1+1, p2+1]
            if s > target:
                p2 -= 1
            if s < target:
                p1 += 1
        return None
    
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
n = int(input())
nums = [int(x) for x in input().split()]
a = int(input())
i = 0
while i != len(nums) - 1:
    if nums[i] == a:
        nums.pop(i)
    else:
        i += 1
print(*nums)

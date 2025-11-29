n = int(input())
nums = list(map(int, input().split()))
index = 0
c = 0
while c != len(nums) - 1:
    if nums[index] == 0:
        nums.append(0)
        nums.pop(index)
    else:
        index += 1
    c += 1

print(*nums)

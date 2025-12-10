def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return (left, right)
        if s < target:
            left += 1
        else:
            right -= 1
    return None


# Пример
print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # (1,3) -> 2+4


def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


# Пример
arr = [1, 1, 2, 2, 3]
k = remove_duplicates(arr)
print(k, arr[:k])  # 3 [1,2,3]

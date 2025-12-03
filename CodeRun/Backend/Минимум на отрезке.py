from collections import deque


def main():
    n, k = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    q = deque()
    for i in range(k):
        while q and nums[q[-1]] >= nums[i]:
            q.pop()
        q.append(i)
    print(nums[q[0]])
    for i in range(k, len(nums)):
        while q and nums[q[-1]] >= nums[i]:
            q.pop()
        while q and q[0] <= i - k:
            q.popleft()
        q.append(i)
        print(nums[q[0]])


if __name__ == "__main__":
    main()

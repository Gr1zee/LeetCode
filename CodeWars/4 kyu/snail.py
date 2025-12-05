def snail(snail_map):
    result = []
    up = 0
    down = len(snail_map)-1
    right = len(snail_map)-1
    left = 0
    if snail_map == [[]]:
        return []
    while up <= down and left <= right:
        for i in range(left, right+1):
            result.append(snail_map[up][i])
        up += 1
        for i in range(up, down+1):
            result.append(snail_map[i][right])
        right -= 1
        if up > down or left > right:
            break
        for i in range(right, left-1, -1):
            result.append(snail_map[down][i])
        down -= 1
        if up > down or left > right:
            break
        for i in range(down, up-1, -1):
            result.append(snail_map[i][left])
        left += 1
    return result

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))
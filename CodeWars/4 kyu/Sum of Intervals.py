def sum_of_intervals(intervals):
    result = 0
    intervals.sort()
    i = 1
    while i < len(intervals):
        if intervals[i][0] < intervals[i-1][1]:
            a = min(intervals[i - 1][0], intervals[i][0])
            b = max(intervals[i][1], intervals[i-1][1])
            intervals.pop(i)
            intervals.pop(i-1)
            intervals.insert(i-1, [a, b])
            i -= 1
        i += 1
    for elem in intervals:
        result += abs(elem[1] - elem[0])
    return result
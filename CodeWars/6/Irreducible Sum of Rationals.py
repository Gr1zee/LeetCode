def sum_fracts(lst):
    N = [x[0] for x in lst]
    D = [x[1] for x in lst]
    d = D[0]
    for i in range(len(D) - 1):
        a = D[i]
        b = D[i + 1]
        while b != 0:
            r = a % b
            a = b
            b = r

from re import *

a = str(input())
p = r"(?:[(]*[)]*)"
pattern = rf"(?:{p}*)"
if a[0] == "(" and a.count("(") == a.count(")"):
    ans = findall(pattern, a)
    if len(ans[0]) == len(a):
        print("right")
    else:
        print("wrong")
else:
    print("wrong")

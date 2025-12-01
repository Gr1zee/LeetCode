import sys


def main():
    d = {}
    for i in range(int(input())):
        k, v = input().split()
        d[k] = v
        d[v] = k
    print(d[input()])


if __name__ == "__main__":
    main()

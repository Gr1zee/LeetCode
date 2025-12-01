import sys


def main():
    st = list(map(int, input.split())).sort()
    if st[-1] < st[0] + st[1]:
        return True
    return False


if __name__ == "__main__":
    main()

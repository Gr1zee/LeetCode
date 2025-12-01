import sys


def main():
    data = sys.stdin.read()
    res = set()
    for elem in data.split():
        res.add(elem)
    print(len(res))


if __name__ == "__main__":
    main()

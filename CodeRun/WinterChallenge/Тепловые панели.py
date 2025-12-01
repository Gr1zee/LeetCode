import sys
import math


def main():
    R, B = [int(x) for x in input().split()]
    S = R // 2 + 2
    D = (S * S) - 4 * (B + R)
    root = math.isqrt(D)
    W = (S + root) // 2
    H = (S - root) // 2
    print(W, H)


if __name__ == "__main__":
    main()

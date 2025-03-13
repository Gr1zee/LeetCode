import math

def find_solutions(a):
    if a == 0:
        return ["0.0000"]
    sol1 = 0.5 * math.sqrt(2 - 2 * math.sqrt(1 - a**2 / (a**2 + 1)))
    sol2 = -sol1
    sol3 = 0.5 * math.sqrt(2 + 2 * math.sqrt(1 - a**2 / (a**2 + 1)))
    sol4 = -sol3

    if a <= 0:
        return [f"{sol2:.4f}", f"{sol3:.4f}"]
    else:
        return [f"{sol4:.4f}", f"{sol1:.4f}"]

def main():
    T = int(input())
    results = []
    for i in range(1, T + 1):
        a = float(input())
        solutions = find_solutions(a)
        if solutions:
            results.append(f"Case#{i}: {' '.join(solutions)}")
        else:
            results.append(f"Case#{i}: No Solution")
    print("\n".join(results))

if __name__ == "__main__":
    main()
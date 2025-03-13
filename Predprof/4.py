import math

def calculate_median_emf(a_cm, n_hz):
    a_m = a_cm / 100
    S = a_m**2
    B = 0.5
    data = []

    t = 0
    while t <= 5.6:
        emf = 2 * math.pi * n_hz * B * S * math.sin(2 * math.pi * n_hz * t)
        data.append(round(emf, 3))
        t += 0.1

    data.sort()
    median = data[len(data) // 2]
    return f"{median:.3f}"

# Input
a_cm, n_hz = map(float, input().split())

# Output
print(calculate_median_emf(a_cm, n_hz))
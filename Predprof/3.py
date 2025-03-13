def calculate_distance_to_proxima(n, M, t_years, k, T_values):
    g = 9.81
    c = 3e8
    seconds_in_year = 365 * 24 * 3600

    # Convert times to seconds
    T_seconds = [T * 7 * 24 * 3600 for T in T_values]
    t_seconds = t_years * seconds_in_year

    # Acceleration phase
    T0 = sum(T_seconds[i] / (2**i) for i in range(1, n + 1))
    R0 = 0.5 * k * g * T0**2
    v_max = k * g * T0

    # Constant speed phase
    r = v_max * t_seconds

    # Deceleration phases
    P = v_max
    R_deceleration = [T_seconds[i] * (P - sum(k * g * T_seconds[j] / (2**j) for j in range(1, i + 1))) for i in range(1, n + 1)]

    # Total distance in meters
    total_distance = R0 + r + sum(R_deceleration)

    # Convert to light years
    distance_light_years = total_distance / (c * seconds_in_year)
    return round(distance_light_years, 2)

# Input
n = int(input())
M = float(input())
t_years = float(input())
k = float(input())
T_values = [float(input()) for _ in range(n)]

# Output
result = calculate_distance_to_proxima(n, M, t_years, k, T_values)
print(result)
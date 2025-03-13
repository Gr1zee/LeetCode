from itertools import permutations
from math import sqrt

def calculate_time_and_distance(points):
    results = []
    for variant in permutations(points, 4):
        dist_1 = sqrt((variant[1][0] - variant[0][0])**2 + (variant[1][1] - variant[0][1])**2)
        dist_2 = sqrt((variant[2][0] - variant[1][0])**2 + (variant[2][1] - variant[1][1])**2)
        dist_3 = sqrt((variant[3][0] - variant[2][0])**2 + (variant[3][1] - variant[2][1])**2)

        t_1 = sqrt(dist_1)  # Time for uniformly accelerated motion
        t_2 = dist_2 / 4    # Time for uniform motion
        t_3 = max(0, -4 + sqrt(16 + 2 * dist_3))  # Time for decelerated motion

        total_distance = dist_1 + dist_2 + dist_3
        total_time = t_1 + t_2 + t_3
        results.append((total_distance, total_time))

    return min(results, key=lambda x: x[1])

# Input
points = [tuple(map(float, input().split(','))) for _ in range(6)]
distance, time = calculate_time_and_distance(points)
print(f"{distance:.2f}")
print(f"{time:.2f}")
import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Invalid input: ensure m ≤ n, d > 0, n ≥ 0, m ≥ 0")

    max_val = 10**d - 1
    array = np.random.randint(0, max_val + 1, size=(n, n))

    start = (n - m) // 2
    end = start + m

    array[start:end, start:end] = -1
    return array

print(replace_center_with_minus_one(2, 5, 3))

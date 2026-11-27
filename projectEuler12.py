import math


def count_divisors(n: int) -> int:
    count = 0
    limit = math.isqrt(n)
    for d in range(1, limit + 1):
        if n % d == 0:
            count += 2 if d * d != n else 1
    return count


def first_triangle_with_over_divisors(threshold: int) -> int:
    n = 1
    while True:
        # T(n) = n * (n + 1) / 2; n and n + 1 are coprime
        if n % 2 == 0:
            divisors = count_divisors(n // 2) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors((n + 1) // 2)
        if divisors > threshold:
            return n * (n + 1) // 2
        n += 1


if __name__ == "__main__":
    print(first_triangle_with_over_divisors(500))

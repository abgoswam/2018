# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_fast(a, b):
    _a = max(a, b)
    _b = min(a, b)

    r = _a % _b
    if r == 0:
        return _b
    else:
        return gcd_fast(_b, r)


def lcm_fast(a, b):
    gcd_a_b = gcd_fast(a, b)
    factor_a = a // gcd_a_b
    factor_b = b // gcd_a_b
    return factor_a * factor_b * gcd_a_b


# Stress Test
import random
def stress_test(a_max, b_max):
    while True:
        a = random.randint(1, a_max)
        b = random.randint(1, b_max)
        lcm_1 = lcm_naive(a, b)
        lcm_2 = lcm_fast(a, b)
        print("{0}, {1}, {2}, {3}".format(a, b, lcm_1, lcm_2))
        assert lcm_1 == lcm_2


if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(lcm_fast(a, b))

    # stress_test(100, 100)

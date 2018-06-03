# Uses python3
import sys
import random

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    _a = max(a, b)
    _b = min(a, b)

    r = _a % _b
    if r == 0:
        return _b
    else:
        return gcd_fast(_b, r)


# Stress Test
def stress_test(a_max, b_max):
    while True:
        a = random.randint(1, a_max)
        b = random.randint(1, b_max)
        gcd_1 = gcd_naive(a, b)
        gcd_2 = gcd_fast(a, b)
        print("{0}, {1}, {2}, {3}".format(a, b, gcd_1, gcd_2))
        assert gcd_1 == gcd_2


if __name__ == "__main__":
    a, b = map(int, input().split())
    # print(gcd_naive(a, b))
    print(gcd_fast(a, b))

    # stress_test(100, 100)

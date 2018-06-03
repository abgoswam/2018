# Uses python3
import sys
import random


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):
    fib_mod10 = [0, 1]
    for i in range(2, n+1):
        x = (fib_mod10[i-1] + fib_mod10[i-2]) % 10
        fib_mod10.append(x)

    return fib_mod10[n]


# Stress Test
def stress_test(N):
    while True:
        n = random.randint(0, N)
        fib_last_slow = get_fibonacci_last_digit_naive(n)
        fib_last_fast = get_fibonacci_last_digit_fast(n)
        print("{0}, {1}, {2}".format(n, fib_last_slow, fib_last_fast))
        assert fib_last_slow == fib_last_fast



if __name__ == '__main__':
    n = int(input())
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))

    # stress_test(10)

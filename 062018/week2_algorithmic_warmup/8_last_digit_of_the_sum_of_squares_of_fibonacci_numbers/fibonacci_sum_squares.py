# Uses python3
from sys import stdin
import random

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_fast(n):
    if n <= 1:
        return n

    fib_mod10 = [0, 1]
    while True:
        x = (fib_mod10[-1] + fib_mod10[-2]) % 10
        fib_mod10.append(x)

        if fib_mod10[-2:] == [0, 1]:
            seq_length = len(fib_mod10) - 2
            break

    fib_squared_mod10 = [0, 1]
    for i in range(2, seq_length+1):
        x = (fib_mod10[i]**2) % 10
        fib_squared_mod10.append(x)

    fib_squared_sum_mod10 = [0, 1]
    for i in range(2, seq_length + 1):
        x = (fib_squared_sum_mod10[-1] + fib_squared_mod10[i]) % 10
        fib_squared_sum_mod10.append(x)

    return fib_squared_sum_mod10[n%seq_length]


def fibonacci_huge(n, m):
    if n <= 1:
        return n

    fib_modm = [0, 1]
    while True:
        x = (fib_modm[-1] + fib_modm[-2]) % m
        fib_modm.append(x)

        if fib_modm[-2:] == [0, 1]:
            seq_length = len(fib_modm) - 2
            break

    return fib_modm[n % seq_length]


def fibonacci_sum_squares_fast_2(n):
    if n <= 1:
        return n

    a = fibonacci_huge(n, 10)
    b = fibonacci_huge(n+1, 10)
    return (a*b) % 10


# Stress Test
def stress_test(n_max):
    while True:
        n = random.randint(0, n_max)
        sq_1 = fibonacci_sum_squares_fast(n)
        sq_2 = fibonacci_sum_squares_fast_2(n)
        print("{0}, {1}, {2}".format(n, sq_1, sq_2))
        assert sq_1 == sq_2



if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_squares_naive(n))
    # print(fibonacci_sum_squares_fast(n)) # works
    print(fibonacci_sum_squares_fast_2(n))
    # stress_test(1000)

# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    fib_mod10 = [0, 1]
    fib_cum_mod10 = [0, 1]
    while True:
        x = (fib_mod10[-1] + fib_mod10[-2]) % 10
        y = (x + fib_cum_mod10[-1]) % 10

        fib_mod10.append(x)
        fib_cum_mod10.append(y)

        if fib_mod10[-2:] == [0, 1]:
            seq_length = len(fib_mod10) - 2
            break

    return fib_cum_mod10[n % seq_length]


if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))

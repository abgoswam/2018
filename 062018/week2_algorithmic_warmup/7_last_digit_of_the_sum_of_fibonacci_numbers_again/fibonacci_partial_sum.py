# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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


def fibonacci_partial_sum_fast(m, n):
    if m == 0:
        sum_m_1 = 0
    else:
        sum_m_1 = fibonacci_sum_fast(m - 1)

    sum_n = fibonacci_sum_fast(n)
    return (sum_n - sum_m_1) % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))

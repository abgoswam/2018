# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    fib_modm = [0, 1]
    seq_found = False
    for i in range(2, n+1):
        x = (fib_modm[i-1] + fib_modm[i-2]) % m
        fib_modm.append(x)
        if fib_modm[len(fib_modm)-2:] == [0, 1]:
            seq_found = True
            break

    if seq_found:
        seq_length = len(fib_modm)-2
        k = n % seq_length
    else:
        # n is smaller than sequence length
        k = n

    return fib_modm[k]


if __name__ == '__main__':
    n, m = map(int, input().split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))

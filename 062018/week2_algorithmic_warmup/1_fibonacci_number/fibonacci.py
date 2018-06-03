# Uses python3

import random

def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    fib = [0, 1]
    for i in range(2, n+1):
        x = fib[i-1] + fib[i-2]
        fib.append(x)

    return fib[n]

# Stress Test
def stress_test(N):
    while True:
        n = random.randint(0, N)
        fib_slow = calc_fib(n)
        fib_fast = calc_fib_fast(n)
        print("{0}, {1}, {2}".format(n, fib_slow, fib_fast))
        assert fib_slow == fib_fast





if __name__ == '__main__':
    n = int(input())
    # print(calc_fib(n))
    print(calc_fib_fast(n))

    # # stress test
    # stress_test(10)

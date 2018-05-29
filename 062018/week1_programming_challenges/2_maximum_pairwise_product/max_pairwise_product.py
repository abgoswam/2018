# python3
import random


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)

    i_max = 0
    for i in range(1, n):
        if numbers[i] > numbers[i_max]:
            i_max = i

    if i_max == 0:
        i_2nd = 1
    else:
        i_2nd = 0

    for i in range(n):
        if i == i_max:
            continue

        if numbers[i] >= numbers[i_2nd]:
            i_2nd = i

    return numbers[i_max] * numbers[i_2nd]


def compare(i_max, i_max2, pi, pi_1, numbers):
    # lets compare the p's first
    if numbers[pi] > numbers[pi_1]:
        p1 = pi
        p2 = pi_1
    else:
        p1 = pi_1
        p2 = pi

    if numbers[i_max] > numbers[p1]:
        cmax = i_max
        if numbers[i_max2] > numbers[p1]:
            cmax2 = i_max2
        else:
            cmax2 = p1
    else:
        cmax = p1
        if numbers[i_max] > numbers[p2]:
            cmax2 = i_max
        else:
            cmax2 = p2

    return cmax, cmax2


def max_pairwise_product_faster(numbers):
    n = len(numbers)

    if numbers[0] > numbers[1]:
        i_max = 0
        i_max2 = 1
    else:
        i_max = 1
        i_max2 = 0

    for i in range(1, (n // 2)):
        i_max, i_max2 = compare(i_max, i_max2, 2 * i, 2 * i + 1, numbers)

    # if n is odd, the above loop will leave out last position.
    # handle it separately
    if n % 2 == 1:
        if numbers[n-1] > numbers[i_max]:
            i_max2 = i_max
            i_max = n-1
        else:
            if numbers[n-1] > numbers[i_max2]:
                i_max2 = n-1

    return numbers[i_max] * numbers[i_max2]


# Testing
def generate_numbers():
    numbers = []
    for i in range(2 * 10 ** 3 + 1):
        numbers.append(i)

    return numbers


# Stress Testing
# 2 <= n <= N
# 0 <= numbers[i] <= M
def stress_test(N, M):
    while True:
        n = random.randint(2, N)

        numbers = []
        for i in range(n):
            _r = random.randint(0, M)
            numbers.append(_r)

        product_naive = max_pairwise_product(numbers)
        product_fast = max_pairwise_product_fast(numbers)
        product_faster = max_pairwise_product_faster(numbers)
        print(n)
        print(numbers)
        print(product_fast, product_faster)
        assert product_fast == product_faster


# stress_test(2*(10**2), 2*(10**2))
# print(max_pairwise_product_faster([0, 2, 1]))

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_faster(input_numbers))

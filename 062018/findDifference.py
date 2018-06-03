import random
import copy

#  assume a is longer array
def find_difference(a, b):
    a.sort()
    b.sort()

    diff = None
    for i in range(len(a)):
        if i == len(a) - 1:
            diff = a[i]
        else:
            if a[i] != b[i]:
                diff = a[i]
                break

    return diff


def find_difference_map(a, b):
    D = {}
    for i in range(len(a)):
        if a[i] in D:
            D[a[i]] += 1
        else:
            D[a[i]] = 1

    for i in range(len(b)):
        D[b[i]] -= 1

    diff = None
    for key in D:
        if D[key] != 0:
            diff = key
            break

    return diff

# Stress test
def stress_test(N, M):
    while True:
        n = random.randint(1, N)
        a = []
        for i in range(n):
            a.append(random.randint(0, M))


        idx = random.randint(0, len(a)-1)
        b = copy.deepcopy(a)
        del(b[idx])

        print(a)
        print(b)

        diff_1 = find_difference(a, b)
        diff_2 = find_difference_map(a, b)
        assert diff_1 == diff_2


stress_test(10, 5)

# if __name__ == '__main__':
#     l1 = [int(x) for x in input().split()]
#     l2 = [int(x) for x in input().split()]
#     print(find_difference(l1, l2))
#     print(find_difference_map(l1, l2))

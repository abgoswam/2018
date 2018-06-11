#Uses python3

import sys
import random

# def largest_number(a):
#     #write your code here
#     res = ""
#     max_d = 0
#     for x in a:
#         if max_d < len(x):
#             max_d = len(x)
#
#     dict = {}
#     for i in range(len(a)):
#         if len(a[i]) == max_d:
#             dict[i] = a[i]
#         else:
#             p = a[i]
#             last_digit = a[i][len(a[i]) - 1]
#             for j in range(len(a[i]), max_d):
#                 p += last_digit
#
#             dict[i] = p
#
#     # print(dict)
#     dict_sorted = sorted(dict.items(), reverse=True, key=lambda x: x[1])
#     # print(dict_sorted)
#
#     for item in dict_sorted:
#         k = item[0]
#         res += a[k]
#
#     return res




def is_a_largerthan_b(a, b):
    if len(a) == len(b):
        return a >= b
    else:
        l = min(len(a), len(b))
        if a[:l] != b[:l]:
            return a[:l] >= b[:l]
        else:
            if len(a) > len(b):
                return is_a_largerthan_b(a[l:], b)
            else:
                return is_a_largerthan_b(a, b[l:])


def largest_number(a):
    answer = ''
    while a:
        max_number_idx = 0
        for i in range(1, len(a)):
            if is_a_largerthan_b(a[i], a[max_number_idx]):
                max_number_idx = i

        answer += a[max_number_idx]
        del a[max_number_idx]

    return answer


def stress_test(N):
    while True:
        a1 = random.randint(1, N)
        a2 = random.randint(1, N)
        a = [str(a1), str(a2)]

        # algo 1
        n1 = int(str(a1) + str(a2))
        n2 = int(str(a2) + str(a1))
        p = max(n1, n2)

        # algo 2
        q = largest_number(a)

        print(a)
        print(p)
        print(q)
        print("--------")
        assert str(p) == q

# print(largest_number(['10', '10']))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

    # stress_test(100)

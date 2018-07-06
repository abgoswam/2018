# Uses python3
import sys
import copy


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here
    return number_of_inversions


def merge_sort(a, b, left, right):
    ni = 0
    if right - left <= 1:
        b[left] = a[left]
        return ni

    mid = (left + right) // 2
    ni += merge_sort(a, b, left, mid)
    ni += merge_sort(a, b, mid, right)

    x = copy.deepcopy(b[left:mid])
    y = copy.deepcopy(b[mid:right])
    x_id = y_id = 0
    b_id = left

    while x_id < len(x) and y_id < len(y):
        if x[x_id] <= y[y_id]:
            b[b_id] = x[x_id]
            x_id += 1
            ni += y_id
        else:
            b[b_id] = y[y_id]
            y_id += 1

        b_id += 1

    while x_id < len(x):
        b[b_id] = x[x_id]
        b_id += 1
        x_id += 1
        ni += y_id

    while y_id < len(y):
        b[b_id] = y[y_id]
        b_id += 1
        y_id += 1

    return ni


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    ni = merge_sort(a, b, 0, len(a))
    print(ni)

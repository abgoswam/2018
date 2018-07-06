# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1, None
    if left + 1 == right:
        return a[left], 1

    #write your code here
    mid = (left + right) // 2

    mL, cL = get_majority_element(a, left, mid)
    mR, cR = get_majority_element(a, mid, right)

    if mL != -1:
        # count instances of mL on right
        count = 0
        for i in range(mid, right):
            if a[i] == mL:
                count += 1

        total = cL + count
        if total > (right - left) / 2:
            return mL, total

    if mR != -1:
        # count instances of mR on left
        count = 0
        for i in range(left, mid):
            if a[i] == mR:
                count += 1

        total = cR + count
        if total > (right - left) / 2:
            return mR, total

    return -1, None


# print(get_majority_element([1, 1, 3, 1], 0, 4))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    # print(n)
    # print(a)

    l, c = get_majority_element(a, 0, n)
    if l != -1:
        print(1)
    else:
        print(0)

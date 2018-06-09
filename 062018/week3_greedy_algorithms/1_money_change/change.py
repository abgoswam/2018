# Uses python3
import sys

def get_change(m):
    #write your code here

    n_10 = m // 10
    r_10 = m % 10

    n_5 = r_10 // 5
    r_5 = r_10 % 5

    n_1 = r_5

    return n_10 + n_5 + n_1


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

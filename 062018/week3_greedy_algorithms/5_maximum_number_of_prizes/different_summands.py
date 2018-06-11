# Uses python3
import sys


def optimal_summands(n):
    summands = []
    # write your code here
    N = 1
    while True:
        if (N*(N+1))/2 <= n < ((N+1)*(N+2))/2:
            break
        N += 1

    summands.extend(list(range(1, N)))
    summands.append(n - ((N-1)*N//2))
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

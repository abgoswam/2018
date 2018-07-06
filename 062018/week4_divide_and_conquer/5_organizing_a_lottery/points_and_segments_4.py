# Uses python3
import sys
import random


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # write your code here

    l = []
    for s in starts:
        l.append((s, 'l', 0))
    for e in ends:
        l.append((e, 'r', 0))
    for k in range(len(points)):
        l.append((points[k], 'p', k))

    ls = sorted(l)

    active = 0
    for p in ls:
        if p[1] == 'p':  # for this case p[2] stored the index this point belongs to
            cnt[p[2]] = active
        elif p[1] == 'l':
            active += 1
        else:
            active -= 1

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt



def stress_test():
    while True:
        s = random.randint(1, 10)
        p = random.randint(1, 10)

        starts = []
        ends = []
        for i in range(s):
            a = random.randint(-100, 100)
            b = random.randint(a, 100)
            starts.append(a)
            ends.append(b)

        points = []
        for i in range(p):
            p = random.randint(-200, 200)
            points.append(p)


        # algo 1: naive_count_segments
        cnt_naive = naive_count_segments(starts, ends, points)

        # algo 2
        cnt_fast = fast_count_segments(starts, ends, points)

        print(starts)
        print(ends)
        print(points)
        print("--------")
        assert cnt_naive == cnt_fast


# stress_test()

# --------------------------------------
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    # starts = [-10]
    # ends = [10]
    # points = [-100, 100, 0]

    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
    print()
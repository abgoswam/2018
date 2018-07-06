# Uses python3
import sys
import random


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # write your code here
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


# -------------------------------
class Segment(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __str__(self):
        return "start:{0} end:{1}".format(self.start, self.end)


class Node(object):
    def __init__(self, x_mid):
        self.x_mid = x_mid
        self.lc = None
        self.rc = None
        self.d_left = None
        self.d_right = None


def intervals(starts, ends):
    n = len(starts)
    segments = []
    D = {}

    for i in range(n):
        if (starts[i], ends[i]) in D:
            D[(starts[i], ends[i])] += 1
        else:
            segments.append(Segment(starts[i], ends[i]))
            D[(starts[i], ends[i])] = 1

    return segments, D


def construct_intervaltree(segments):
    if segments is None or len(segments) == 0:
        return None

    x = []
    for s in segments:
        x.append(s.start)
        x.append(s.end)

    x.sort()
    x_mid = x[len(x)//2]

    i_left = []
    i_right = []
    i_mid = []
    for seg in segments:
        if seg.start < x_mid and seg.end < x_mid:
            i_left.append(seg)
        elif x_mid < seg.start and x_mid < seg.end:
            i_right.append(seg)
        else:
            i_mid.append(seg)

    v = Node(x_mid)
    v.lc = construct_intervaltree(i_left)
    v.rc = construct_intervaltree(i_right)
    v.d_left = sorted(i_mid, key=lambda x: x.start)
    v.d_right = sorted(i_mid, key=lambda x: x.end, reverse=True)

    return v


def containing_intervals(v, qx, D):
    if v is None:
        return 0

    c_intervals = 0
    if qx < v.x_mid:
        for i in range(len(v.d_left)):
            it = v.d_left[i]
            if qx < it.start:
                break

            if it.start <= qx <= it.end:
                c_intervals += D[(it.start, it.end)]

        c_intervals += containing_intervals(v.lc, qx, D)
    else:
        for i in range(len(v.d_right)):
            it = v.d_right[i]
            if it.end < qx:
                break
            if it.start <= qx <= it.end:
                c_intervals += D[(it.start, it.end)]

        c_intervals += containing_intervals(v.rc, qx, D)

    return c_intervals


def intervaltree_count_segments(starts, ends, points):
    # construct intervals
    S, D = intervals(starts, ends)

    # construct intervaltree
    it = construct_intervaltree(S)

    cnt = [0] * len(points)
    for i in range(len(points)):
        cnt[i] = containing_intervals(it, points[i], D)

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
        cnt_intervaltree = naive_count_segments(starts, ends, points)

        print(starts)
        print(ends)
        print(points)
        print("--------")
        assert cnt_naive == cnt_intervaltree


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

    # use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
    # print()

    cnt = intervaltree_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
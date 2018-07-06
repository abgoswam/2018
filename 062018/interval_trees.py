import sys


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


def containing_intervals(v, qx):
    if v is None:
        return None

    c_intervals = []
    if qx < v.x_mid:
        for i in range(len(v.d_left)):
            it = v.d_left[i]
            if qx < it.start:
                break

            if it.start <= qx <= it.end:
                c_intervals.append(it)

        inter = containing_intervals(v.lc, qx)
        if inter is not None:
            c_intervals.extend(inter)
    else:
        for i in range(len(v.d_right)):
            it = v.d_right[i]
            if it.end < qx:
                break
            if it.start <= qx <= it.end:
                c_intervals.append(it)

        inter = containing_intervals(v.rc, qx)
        if inter is not None:
            c_intervals.extend(inter)

    return c_intervals


def intervals(starts, ends):
    n = len(starts)
    segments = []
    for i in range(n):
        segments.append(Segment(starts[i], ends[i]))

    return segments


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = len(data)
    # starts = data[0:n:2]
    # ends = data[1:n:2]

    starts = [1, 2, 0, 8, 9, 10]
    ends = [11, 9, 6, 9, 10, 11]

    # construct segments
    S = intervals(starts, ends)

    # display segments
    for seg in S:
        print(seg)

    # construct tree
    it = construct_intervaltree(S)

    for pt in [4]:
        pt_intvs = []
        pt_intvs.extend(containing_intervals(it, pt))
        for pt_int in pt_intvs:
            print(pt_int)

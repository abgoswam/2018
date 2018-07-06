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
class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def get_begin(self):
        return self.begin

    def get_end(self):
        return self.end

    def __str__(self):
        return "start:{0} end : {1}".format(self.begin, self.end)


class Node:
    def __init__(self, x_center, s_center, left_node, right_node):
        self.x_center = x_center
        self.s_center = sort_by_begin(s_center)
        self.left_node = left_node
        self.right_node = right_node


def sort_by_begin(intervals):
    return sorted(intervals, key=lambda x: x.get_begin())


class IntervalTree:
    def __init__(self, intervals):
        self.top_node = self.divide_intervals(intervals)

    def divide_intervals(self, intervals):
        if not intervals:
            return None

        x_center = self.center(intervals)
        s_center = []
        s_left = []
        s_right = []

        for k in intervals:
            if k.get_end() < x_center:
                s_left.append(k)
            elif k.get_begin() > x_center:
                s_right.append(k)
            else:
                s_center.append(k)

        return Node(
            x_center,
            s_center,
            self.divide_intervals(s_left),
            self.divide_intervals(s_right))

    def center(self, intervals):
        fs = sort_by_begin(intervals)
        length = len(fs)
        return fs[length//2].get_begin()

    def _search(self, node, point, result):
        for k in node.s_center:
            if k.get_begin() <= point <= k.get_end():
                result.append(k)

        if point < node.x_center and node.left_node:
            temp = self._search(node.left_node, point, [])
            result.extend(temp)

        if point > node.x_center and node.right_node:
            temp = self._search(node.right_node, point, [])
            result.extend(temp)

        return list(set(result))


def intervaltree_count_segments(starts, ends, points):
    # construct intervals
    intervals = []
    for i in range(len(starts)):
        intervals.append(Interval(starts[i], ends[i]))

    # construct tree
    it = IntervalTree(intervals)

    cnt = [0] * len(points)
    for i in range(len(points)):
        result = it._search(it.top_node, points[i], [])
        cnt[i] = len(result)

    return cnt


# -------------------------------
def stress_test():
    while True:
        s = random.randint(1, 10)
        p = random.randint(1, 10)

        starts = []
        ends = []
        for i in range(s):
            a = random.randint(-100, 100)
            b = random.randint(a, 200)
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
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


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = len(data)
    # starts = data[0:n:2]
    # ends = data[1:n:2]

    starts = [1, 2, 0, 8, 9, 10]
    ends = [11, 9, 6, 9, 10, 11]

    # construct intervals
    intervals = []
    for i in range(len(starts)):
        intervals.append(Interval(starts[i], ends[i]))


    # construct tree
    it = IntervalTree(intervals)

    for pt in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        result = it._search(it.top_node, pt, [])
        print("For {0} --------------".format(pt))
        for item in result:
            print(item)


# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):

    points = []

    segments_sorted = sorted(segments, key=lambda s: s.end)

    while len(segments_sorted) > 0:
        p = segments_sorted[0].end
        points.append(p)
        segments_sorted = [item for item in segments_sorted if item.start > p]

    return points


def optimal_points_2(segments):
    n = len(segments)
    points = []

    segments_sorted = sorted(segments, key=lambda s: s.end)

    i = 0
    while i < n:
        p = segments_sorted[i].end

        #  skip over points which u can
        while (i+1) < n and segments_sorted[i+1].start <= p:
            i += 1

        i += 1
        points.append(p)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points_2(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

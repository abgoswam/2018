# Uses python3
import sys
import operator as op


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    value_per_unit_weight = {}
    for i in range(len(weights)):
        vw = values[i] / weights[i]
        value_per_unit_weight[i] = vw

    sorted_vw = sorted(value_per_unit_weight.items(), key=op.itemgetter(1), reverse=True)

    for i in range(len(sorted_vw)):
        w_i = weights[sorted_vw[i][0]]
        v_i = values[sorted_vw[i][0]]
        vw_i = sorted_vw[i][1]

        if capacity >= w_i:
            capacity -= w_i
            value += v_i
        else:
            value += (capacity * vw_i)
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# Uses python3
import sys
import random
import copy

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def opt_sequence(n):
    seq = {1: [1], 2: [1, 2], 3: [1, 3]}

    for i in range(4, n + 1):
        s1 = seq[i-1]
        s2 = s3 = None
        if i % 2 == 0:
            s2 = seq[i//2]
        if i % 3 == 0:
            s3 = seq[i // 3]

        if s2 is None and s3 is None:
            # just s1 to consider
            seq_selected = s1
        elif s2 is None:
            # s1 and s3 to consider
            if len(s1) < len(s3):
                seq_selected = s1
            else:
                seq_selected = s3
        elif s3 is None:
            # s1 and s2 to consider
            if len(s1) < len(s2):
                seq_selected = s1
            else:
                seq_selected = s2
        else:
            # all three (S1, s2, s3) to consider
            if len(s1) < len(s2):
                if len(s1) < len(s3):
                    seq_selected = s1
                else:
                    seq_selected = s3
            else:
                if len(s2) < len(s3):
                    seq_selected = s2
                else:
                    seq_selected = s3

        # note: its crucial we use 'copy' here
        l = copy.copy(seq_selected)
        l.append(i)
        seq[i] = l

    return seq[n]


def stress_test():
    for r in range(1, 1000):
        seq1 = list(optimal_sequence(r))
        seq2 = opt_sequence(r)
        print(r)
        print(seq1)
        print(seq2)
        assert len(seq1) == len(seq2)
        print("--------------------")


# for i in range(1, 10):
#     print(i)
#     print(opt_sequence(i))
#
# stress_test()

input = sys.stdin.read()
n = int(input)
sequence = list(opt_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

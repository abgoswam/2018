def sample_func(*args):
    smaple = sum(args) # note the misspelling of `sample here`
    sample = 10
    print(sample * sample)

def sample_func2(sample):
    sample = 10
    print(sample * sample)


if __name__ == "__main__":
    for sample in range(1, 5):
        sample_func()

    print(sample)
# iterative approach


def add1_iterative(numeric_array):
    if numeric_array is None:
        return None

    print(numeric_array)

    fixed = False
    for i in range(len(numeric_array)-1, -1, -1):
        if 0 <= numeric_array[i] < 9:
            numeric_array[i] += 1
            fixed = True
            break
        else:
            numeric_array[i] = 0

    if fixed is False:
        numeric_array = [1] + numeric_array

    return numeric_array


def add1_recursive(numeric_array):
    if numeric_array is None:
        return None

    if len(numeric_array) == 1:
        if numeric_array[0] == 9:
            return [1, 0]
        else:
            return [numeric_array[0]+1]

    l = len(numeric_array)
    if numeric_array[l-1] == 9:
        return add1_recursive(numeric_array[:l-1]) + [0]
    else:
        numeric_array[l-1] += 1
        return numeric_array


array = [9, 9]
plus1_iter = add1_iterative(array)
print(array)
print(plus1_iter)

print("--------")

array = [9, 9]
plus1_rec = add1_recursive(array)
print(array)
print(plus1_rec)

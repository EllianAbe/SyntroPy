arrays = [
    [5, 3, 8, 1, 9, 6, 7, 2, 4, 0],  # Random order
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],  # Reverse sorted
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Already sorted
    [2, 3, 5, 7, 1, 4, 6, 9, 8, 10],  # Nearly sorted
    [9, 1, 9, 1, 9, 1, 9, 1, 9, 1],  # Repeated elements
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # All elements are the same
    [100, -1, 50, 0, -50, 25, -25, 10, -10, 5],  # Positive and negative numbers
    [8, 5, 9, 2, 7, 1, 3, 6, 0, 4],  # Random order
    [1000, 200, 30, 4, 5000, 60, 700, 8, 900, 10],  # Large numbers
    [5, 5, 5, 4, 4, 4, 3, 3, 3, 2],  # Descending blocks of repeated elements
]


def position_sort(arr, inplace=False):
    if not inplace:
        arr = arr.copy()

    counter = 0
    size = len(arr)

    for i in range(size + 1):
        for j in range(1, size-i):
            counter += 1

            if arr[i] > arr[-j]:
                arr[i], arr[-j] = arr[-j], arr[i]

    return arr


def mysort(arr: list, inplace=False):
    if not inplace:
        arr = arr.copy()

    counter = 0
    size = len(arr)

    i = 0

    while True:
        if i >= size:
            break

        checks = 1
        j = 1

        while j < size:

            for k in range(checks):
                print(f'{arr} i: {i}, j: {j}, k: {k}')
                counter += 1
                ik = i + k

                if ik + j >= size:
                    break

                if arr[ik] > arr[-j]:
                    checks += 1
                    arr[ik], arr[-j] = arr[-j], arr[ik]
                    break

            j += 1

        i += 1

    print(counter)
    return arr


if __name__ == '__main__':

    for idx, arr in enumerate(arrays, start=1):
        print(mysort(arr))
        print(('*'*40+'\n')*3)

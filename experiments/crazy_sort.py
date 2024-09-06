arr = [3, 2, 1, 6, 5, 4, 9, 8, 7]
arr2 = [4, 9, 7, 5, 2, 3, 8, 6, 1]


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


if __name__ == '__main__':
    position_sort(arr2)

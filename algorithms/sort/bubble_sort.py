# given a list of numbers, sort them in ascending order

input = [5, 3, 6, 2, 10]


def bubble_sort(arr):
    arr = arr.copy()
    print(arr)

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)


def swapped_bubble_sort(arr):
    arr = arr.copy()
    print(arr)

    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(arr)


bubble_sort(input)
print('*' * 20)
swapped_bubble_sort(input)

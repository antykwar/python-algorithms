def quick_sort(chaos_list, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(chaos_list) - 1

    if start >= end:
        return

    p = partition(chaos_list, start, end)
    quick_sort(chaos_list, start, p - 1)
    quick_sort(chaos_list, p + 1, end)


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high


test_array = [2, 8, 1, 17, -1, 11, 44, 22, 11, 0, 82, 12]
quick_sort(test_array)
print(test_array)

def find_kth_largest_numbers(arr, k):
    build_heap(arr)
    for i in range(len(arr)-1, len(arr)-1-k, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)
    return arr[len(arr)-k]


def build_heap(arr):
    length = len(arr)
    for i in range((length - 1) // 2, -1, -1):
        max_heapify(arr, i, length)

def max_heapify(arr, i, length):
    left = i * 2 + 1
    right = i * 2 + 2
    if left < length and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
    if right < length and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[larget]
        max_heapify(arr, largest, length)



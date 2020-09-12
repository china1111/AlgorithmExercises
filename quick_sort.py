'''
def test1(lis, first, last):
    if first >= last:
        return
    t = lis[first]
    i = first
    j = last
    while i < j:
        while lis[j] >= t and j != i:
            j -= 1
        if i == j:
            break
        lis[i] = lis[j]
        while lis[i] <=t and j != i:
            i += 1
        if i == j:
            break
        lis[j] = lis[i]
    lis[i] = t
    test1(lis, first, i-1)
    test1(lis, i+1, last)


a = [9,8,7,6,5,4,3,2,1]
test1(a, 0, len(a)-1)
print(a)
'''

'''
def quick_sort(arr):
    if arr == []:
        return arr
    left = quick_sort([i for i in arr[1:] if i < arr[0]])
    right = quick_sort([i for i in arr[1:] if i >= arr[0]])
    return left + [arr[0]] + right
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
result_list = quick_sort(arr)
print(result_list)
print(arr)
'''

'''
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


a = [9,8,7,6,5,4,3,2,1]
quick_sort(a, 0, len(a)-1)
print(a)
'''

'''
def quick_sort(arr):
    return(arr if (arr == None or len(arr) <= 1) else quick_sort([i for i in arr[1:] if i < arr[0]]) + [arr[0]] + quick_sort([i for i in arr[1:] if i >= arr[0]]))

a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = quick_sort(a)
print(b)
'''



def quick_sort(arr, left, right):
    if left >= right:
        return
    i = left
    j = right
    t = arr[left]
    while i < j:
        if arr[j] >= t and i < j:
            j =- 1
        arr[i] = arr[j]
        if arr[i] < t and i < j:
            i += 1
        arr[j] = arr[i]
    arr[i] = t
    quick_sort(arr, left, i - 1)
    quick_sort(arr, i + 1, right)

a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
quick_sort(a, 0, len(a)-1)
print(a)

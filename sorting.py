# O(N^2) Sorting Algorithms - Sequential and comparison based sorting algorithms
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


# O(NlogN) Sorting Algorithms - Recursion based sorting algorithms
def merge_sort(arr):
    # Escape routine
    if len(arr) == 1:
        return arr
    # Decomposition
    tmp_arr1 = []
    tmp_arr2 = []
    for i in range(len(arr)):
        if i < len(arr) / 2:
            tmp_arr1.append(arr[i])
        else:
            tmp_arr2.append(arr[i])
    # Recursion
    tmp_arr1 = merge_sort(tmp_arr1)
    tmp_arr2 = merge_sort(tmp_arr2)
    # Aggregation
    idx_count1 = 0
    idx_count2 = 0
    for i in range(len(arr)):
        if idx_count1 == len(tmp_arr1):
            arr[i] = tmp_arr2[idx_count2]
            idx_count2 += 1
        elif idx_count2 == len(tmp_arr2):
            arr[i] = tmp_arr1[idx_count1]
            idx_count1 += 1
        elif tmp_arr1[idx_count1] > tmp_arr2[idx_count2]:
            arr[i] = tmp_arr2[idx_count2]
            idx_count2 += 1
        else:
            arr[i] = tmp_arr1[idx_count1]
            idx_count1 += 1
    return arr


def quick_sort(arr, idx_pivot=0):
    if len(arr) <= 1:
        return arr

    pivot_value = arr[idx_pivot]
    less = []
    greater = []
    for i in range(len(arr)):
        if i == idx_pivot:
            continue
        if arr[i] > pivot_value:
            greater.append(arr[i])
        else:
            less.append(arr[i])

    return quick_sort(less) + [pivot_value] + quick_sort(greater)


# O(N) Sorting Algorithms - Not comparison-based approach
def counting_sort(arr):
    """Count the occurrence and produce a sequence based upon the counts

    Assumption : The sequence contain integers ranging form 0 to K

    Time complexity: O(N+R), R is the range of the sequence values(maximum value)
    """
    _max = -9999
    _min = 9999
    for i in range(len(arr)):
        if arr[i] > _max:
            _max = arr[i]
        if arr[i] < _min:
            _min = arr[i]

    counting = [0 for i in range(_max - _min + 1)]
    for i, value in enumerate(arr):
        counting[value - _min] += 1

    cnt = 0
    for i in range(_max - _min + 1):
        for _ in range(counting[i]):
            arr[cnt] = i + _min
            cnt += 1

    return arr




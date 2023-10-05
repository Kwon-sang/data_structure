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

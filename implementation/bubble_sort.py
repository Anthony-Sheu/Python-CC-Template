def bubble_sort(arr, n):  # sort in increasing order
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]: arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
###################################################
def bubble_sort(arr, n):  # sort in decreasing order
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j + 1]: arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
###################################################
def bubble_sort(arr, n):  # sort in increasing and count swaps
    c = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j + 1]: arr[j], arr[j + 1] = arr[j + 1], arr[j]; c += 1
    return c

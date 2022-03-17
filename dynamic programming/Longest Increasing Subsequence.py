def lis(arr, n):
    temp = [arr[0]]
    for i in range(1, n):
        if arr[i] > temp[-1]: temp.append(arr[i])
        else: temp[__import__('bisect').bisect_left(temp, arr[i])] = arr[i]
    return len(temp)

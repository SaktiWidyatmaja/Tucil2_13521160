def partition(arr, left, right):
    pivot = arr[right][0]
    i = left - 1
    for j in range(left, right):
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

def quicksort(arr, left, right):
    if left < right:
        id = partition(arr, left, right)
        quicksort(arr, left, id-1)
        quicksort(arr, id+1, right)
def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = arr[0]
        smallest_index = 0
        for j in range(1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        new_arr.append(arr.pop(smallest_index))  
    return new_arr

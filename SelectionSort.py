def selectionSort(arr):
    """
    Sort a list `arr` using the selection sort algorithm by building a new sorted list.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new sorted list with elements in ascending order.
    """
    new_arr = []  # Initialize an empty list to store the sorted elements
    for i in range(len(arr)):
        # Assume the first element is the smallest initially
        smallest = arr[0]
        smallest_index = 0
        # Find the smallest element in the remaining unsorted list
        for j in range(1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        # Remove the smallest element from the original list and append it to the sorted list
        new_arr.append(arr.pop(smallest_index))
    return new_arr  # Return the newly sorted list

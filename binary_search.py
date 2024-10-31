def binary_search(lst, item):
    """
    Perform a binary search to find the index of `item` in the sorted list `lst`.

    Parameters:
    lst (list): A sorted list of elements where the search is to be performed.
    item: The element to search for in the list.

    Returns:
    int or None: The index of the `item` in `lst` if found; otherwise, None.
    """
    low = 0  # Initialize the lower bound of the search range
    high = len(lst) - 1  # Initialize the upper bound of the search range

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        guess = lst[mid]  # Get the middle element
        
        if guess == item:
            return mid  # Return the index if the item is found
        if guess > item:
            high = mid - 1  # Narrow the search range to the lower half
        else:
            low = mid + 1  # Narrow the search range to the upper half
    
    return None  # Return None if the item is not found

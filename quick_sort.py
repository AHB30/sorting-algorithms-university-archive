def quick_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the Quick Sort algorithm.
    
    Args:
        arr (List[int]): The list to be sorted.
        
    Returns:
        List[int]: A new sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
l = [3, 2, 0, 1, 5, 8, 7, 6, 9, 4]
sorted_list = quick_sort(l)
print(sorted_list)

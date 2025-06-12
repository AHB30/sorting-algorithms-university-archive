def insertion_sort(array,debug=False):
    """
       Sorts the input list in ascending order using insertion sort.

       Args:
           array (list): The list to sort.
           debug (bool): If True, prints the sorting steps.
    """
    it = 0
    for i in range(1,len(array)):
        while i > 0 and array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            if debug:
                print(array)
            i -= 1
        if debug:
            print('out of while')
            print(f'______{it}')
        it += 1

arr = [7, 9, 5, 4, 2, 9, 3, 4]
insertion_sort(arr, debug=True)
print("sorted array:", arr)

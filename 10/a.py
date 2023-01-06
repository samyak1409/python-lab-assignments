"""
Write a program to implement Merge sort.
"""


from typing import List


def merge_sort(arr: List[int]) -> None:
    """
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

    Article: https://www.geeksforgeeks.org/merge-sort
    Video: https://youtu.be/JSceec-wEyw
    """

    arr_len = len(arr)
    if arr_len > 1:  # if array has at least 2 elements, we'll divide and sort, otherwise obviously an array with only one element is already sorted

        # Dividing:
        mid_index = arr_len // 2
        left, right = arr[:mid_index], arr[mid_index:]  # dividing the array in 2 sub arrays
        # Recurse: Further dividing until arr have only 1 element:
        merge_sort(arr=left), merge_sort(arr=right)  # IMP: as the reference is passed, left and right will be modified!

        # Merging:
        i = j = 0
        while i < len(left) and j < len(right):
            # Comparing elements of left and right sub array one by one:
            if left[i] <= right[j]:  # '=' is for stable sorting
                arr[i+j] = left[i]
                i += 1
            else:
                arr[i+j] = right[j]
                j += 1
        # Adding remained elements (if any):
        arr[i+j:] = left[i:] or right[j:]


if __name__ == '__main__':

    from random import randint

    size = int(input('\nArray Size: '))
    array = [randint(-size, size) for _ in range(size)]
    """
    print('Unsorted:', array)
    merge_sort(arr=array)
    print('Sorted:', array)
    """
    # Do not want the array to be modified? Just do it the following way:
    array2 = array.copy()  # IMP: copy(), so that input array ("array") is not modified while modifying array2
    merge_sort(arr=array2)
    print('Unsorted:', array)
    print('Sorted:', array2)

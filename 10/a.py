# Write a program to implement Merge sort.


# https://youtu.be/JSceec-wEyw


from random import randint


n = int(input('\nArray Size: '))
l = [randint(-n, n) for _ in range(n)]
print('Unsorted:', l)


def merge_sort(arr):

    len_ = len(arr)
    if len_ > 1:  # if array has at least 2 elements

        # Dividing:
        mid = len_ // 2
        left, right = arr[:mid], arr[mid:]  # dividing the array in 2 sub arrays
        merge_sort(left)  # further dividing left sub array
        merge_sort(right)  # further dividing right sub array

        # Sorting (Merging):
        i = j = 0
        while i < len(left) and j < len(right):
            # Comparing elements of left and right sub array one by one:
            if left[i] < right[j]:
                arr[i+j] = left[i]
                i += 1
            else:
                arr[i+j] = right[j]
                j += 1
        # Adding remained elements (if any):
        arr[i+j:] = left[i:] or right[j:]

    return arr


print('Sorted:', merge_sort(arr=l))

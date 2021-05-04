def binarysearch_iterative(A, key):
    l = 0
    r = len(A) - 1
    count = 0
    while l <= r:
        mid = (l + r) // 2
        if key == A[mid]:
            print("looped",count,"times to find the index position")
            return mid
        elif key < A[mid]:
            r = mid - 1
        elif key > A[mid]:
            l = mid + 1
        count = count + 1
    return -1 #key not in array


A = sorted([10, 200, 12, 213, 434, 23, 11, 13, 14, 9, 90, 103, 323, 40, 30, 949, 48, 384, 383, 1, 2, 3, 4, 5, 6, 7])

print("Sorted Array is: ", A)
key = int(input("What number would you like to know the index position of?"))

ipos = binarysearch_iterative(A, key)
if ipos == -1:
    print ("number was not in the list")
else:
    print ("Index position was", ipos)

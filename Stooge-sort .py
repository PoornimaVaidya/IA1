# Stooge-sort implementation
def stoogesort(A, i, j):
    if i >= j:
        return
    
    if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]
    
    if j - i + 1 > 2:
        m = (j - i + 1) // 3
        stoogesort(A, i, j - m)
        stoogesort(A, i + m, j)
        stoogesort(A, i, j - m)


# Testing stoogesort with n=0, 1, 10, 500
import random
for n in [0, 1, 10, 500]:
    arr = [random.uniform(0, 1) for _ in range(n)]
    print(f"Unsorted array (n={n}): {arr}")
    stoogesort(arr, 0, len(arr) - 1)
    print(f"Sorted array (n={n}): {arr}\n")

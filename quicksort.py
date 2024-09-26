def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)



import random
# Testing quicksort
for n in [0, 1, 10, 500]:
    arr = [random.uniform(0, 1) for _ in range(n)]
    print(f"Unsorted array (n={n}): {arr}")
    print("-----------")
    sorted_arr = quicksort(arr)
    print(f"Sorted array (n={n}): {sorted_arr}\n")
    print("-----------------------------------------------")

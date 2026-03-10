import time
import random

# Generate sample data: 320 random integers between 1 and 9999
random.seed(42)
data = [random.randint(1, 9999) for _ in range(320)]
print(f"Original (first 20): {data[:20]} ...\n")

# Bubble Sort: simple comparison-based sorting
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Merge Sort: divide-and-conquer sorting
def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

# Quick Sort: partition-based divide-and-conquer
def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# Dictionary of algorithms to run
algorithms = {
    "Bubble Sort": bubble_sort,
    "Merge Sort":  merge_sort,
    "Quick Sort":  quick_sort,
}

# Run each sorting algorithm and measure execution time
for name, fn in algorithms.items():
    start = time.time()
    sorted_data = fn(data)
    end = time.time()
    elapsed = end - start

    print(f"Algorithm : {name}")
    print(f"Time      : {elapsed:.6f} seconds")
    print(f"Sorted    : {sorted_data[:20]} ... (first 20 of {len(sorted_data)})")
import random
import time
import matplotlib.pyplot as ply

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

        
def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[low], arr[j] = arr[j], arr[low]
    return j


arr = [5, 8, 1, 2, 6, 3, 9]
print("Before sorting:", arr)

quick_sort(arr, 0, len(arr) - 1)
print("After sorting:", arr)

n_values = [5000, 10000, 15000, 20000, 25000, 30000]
time_taken = []

for n in n_values:
    arr = [random.randint(1, 100000) for _ in range(n)]

    start = time.time()
    quick_sort(arr, 0, n - 1)
    end = time.time()

    elapsed = end - start
    time_taken.append(elapsed)

    print(f"n = {n}, Time Taken = {elapsed:.6f} seconds")


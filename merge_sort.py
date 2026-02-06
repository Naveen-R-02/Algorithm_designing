import random
import time
import matplotlib.pyplot as plt




# MERGE SORT 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    return merge(left, right)




def merge(left, right):
    result = []
    i = j = 0


    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)


# TIME ANALYSIS
n_values = [5000, 10000, 15000, 20000, 25000, 30000]
time_taken = []


for n in n_values:
    arr = [random.randint(1, 100000) for _ in range(n)]


    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()


    elapsed_time = end_time - start_time
    time_taken.append(elapsed_time)


    print(f"n = {n}, Time Taken = {elapsed_time:.6f} seconds")
 
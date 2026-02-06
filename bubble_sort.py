import random as r
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0,n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

n = 5000
arr = [r.randint(1,5000) for _ in range(n)]
print(bubble_sort(arr))



# arr = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(arr))

#step 1: Start
#step 2: Read the number of elements n
#step 3: Read the array elements
#step 4: Repeat steps 5–7 for i = 0 to n-2
#step 5: Repeat steps 6–7 for j = 0 to n-i-2
#step 6: If array[j] > array[j+1], swap them
#step 7: End inner loop
#step 8: End outer loop
#step 9: Display the sorted array
#step 10: Stop
# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        left_half = arr[:mid] 
        right_half = arr[mid:]  

        merge_sort(left_half)  
        merge_sort(right_half) 

        i = j = k = 0


        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

       
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

       
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

import timeit


test_data_small = [5, 2, 9, 1, 5, 6]
test_data_medium = [i for i in range(1000, 0, -1)]  
test_data_large = [i for i in range(100000, 0, -1)] 


def test_merge_sort():
    merge_sort(test_data_small)

def test_insertion_sort():
    insertion_sort(test_data_small)

def test_timsort():
    sorted(test_data_small)


print("Малий масив (Merge Sort):", timeit.timeit(test_merge_sort, number=1000))
print("Малий масив (Insertion Sort):", timeit.timeit(test_insertion_sort, number=1000))
print("Малий масив (Timsort):", timeit.timeit(test_timsort, number=1000))


print("\nСередній масив (Merge Sort):", timeit.timeit(test_merge_sort, number=100))
print("Середній масив (Insertion Sort):", timeit.timeit(test_insertion_sort, number=100))
print("Середній масив (Timsort):", timeit.timeit(test_timsort, number=100))


print("\nВеликий масив (Merge Sort):", timeit.timeit(test_merge_sort, number=10))
print("Великий масив (Insertion Sort):", timeit.timeit(test_insertion_sort, number=10))
print("Великий масив (Timsort):", timeit.timeit(test_timsort, number=10))


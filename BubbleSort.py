import datetime
import random


def bubble_sort(array):
    t1 = datetime.datetime.now()
    
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    t2 = datetime.datetime.now()
    print(t2-t1)
    return array

# arr = [12, 11, 13, 5, 6, 9, 2, 12, 10, 3]


# insertionSort(arr)
# print(arr)
arr = [random.randint(1, 1000000) for x in range(0, 100000)]
bubble_sort(arr) 
# print("Відсортований масив: ", arr, sep='\n')
import datetime
import random

# print(datetime.datetime.now())



def insertionSort(arr):
    t1 = datetime.datetime.now()
    
    n = len(arr)
      
    if n <= 1:
        return
 
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    # time.sleep(2.1)
    
    t2 = datetime.datetime.now()
    print(t2-t1)
    return arr
  

# arr = [12, 11, 13, 5, 6, 9, 2, 12, 10, 3]

arr = [random.randint(1, 1000000) for x in range(0, 50000)]
insertionSort(arr)
# print(arr)
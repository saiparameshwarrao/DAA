def insertion_sort(arr):
    l = len(arr)
    for i in range(l):
        key = arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key                        
    print(arr)

arr = [12, 11, 13, 5, 6, 1, 2]
insertion_sort(arr)
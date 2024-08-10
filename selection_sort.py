def selection_sort(arr):
    l = len(arr)
    for i in range(l-1):
        min = i
        for j in range(i+1,l):
            if (arr[j] < arr[min]):
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    

arr = [6,8,2,3,1]
selection_sort(arr)
print(arr) 




    



    
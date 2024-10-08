def quick_sort(arr,first,last):
    if first < last :
        pivot = first
        j = last
        i=first
        while i<j:
            while arr[i]<=arr[pivot] and i<last:
                i+=1
            while arr[j] > arr[pivot]:
                j-=1
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
        arr[pivot],arr[j] = arr[j],arr[pivot]
        
        quick_sort(arr,first,j-1)
        
        quick_sort(arr,j+1,last)
    
    
    
arr = [9,3,4,1,8,2,5]
n = len(arr)
quick_sort(arr,0,n-1)
print("Sorted array",arr)
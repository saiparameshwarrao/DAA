def priority_number_sort(arr,l):
    for i in range(l):
        key = arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key 
    print("After Sorting Orders Priority:",arr)  
        
        
if __name__ == '__main__':
    priority_number_array = []
    num = int(input("Enter number of priority numbers: "))
    for _ in range(num):
        val = int(input("Enter orders Priority Number: "))
        priority_number_array.append(val)
    priority_number_sort(priority_number_array,num)
    
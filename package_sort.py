def package_sort(arr,l):
    choice = int(input('Do you want asc(1) or desc(2): '))    
    for i in range(l):
        for j in range(l-1):
            if choice == 1:
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
            elif choice == 2:
                if arr[j] < arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
    print("Time in sorted order")
    print(arr)
    
    
if __name__ == "__main__":
    time_array = []
    num = int(input("Enter number of times: "))
    for _ in range(num):
        val = int(input("Enter time to reach destination: "))
        time_array.append(val)
    package_sort(time_array,num)
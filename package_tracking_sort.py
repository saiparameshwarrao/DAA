def package_tracking_sort(arr):
    l = len(arr)
    for i in range(l-1):
        min_index = i
        for j in range(i+1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    print("Sorted tracking numbers:", arr)
    
if __name__ == '__main__':
    tracking_array = []
    num = int(input("Enter number of traking numbers: "))
    for _ in range(num):
        val = int(input("Enter Package Tracking Number: "))
        tracking_array.append(val)
    package_tracking_sort(tracking_array)

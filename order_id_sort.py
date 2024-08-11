def order_id_sort(arr,l):
    for i in range(1, l):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print("After Sorting Orders Priority:",arr)


    
if __name__ == '__main__':
    order_id_array = []
    num = int(input("Enter n: "))
    for _ in range(num):
        val = int(input("Enter orders Priority Number:"))
        order_id_array.append(val)
    order_id_sort(order_id_array,num)

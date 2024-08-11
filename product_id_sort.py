def product_id_sort(arr,l):
    for i in range(l-1):
        min_index = i
        for j in range(i+1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    print("", arr)
    
    
    
if __name__ == '__main__':
    product_id_array = []
    num = int(input("Enter number of id's: "))
    for _ in range(num):
        val = int(input("Enter Products IDs: "))
        product_id_array.append(val)
    product_id_sort(product_id_array,num)

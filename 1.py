def price_sort(arr):
    l = len(arr)
    choice = int(input('Do you want asc(1) or desc(2): '))    
    for i in range(l-1):
        min_index = i
        for j in range(i+1, l):
            if choice == 1:
                if arr[j] < arr[min_index]:
                    min_index = j
            elif choice == 2:
                if arr[j] > arr[min_index]:
                    min_index = j
            else:
                print("Invalid choice. Please enter 1 for ascending or 2 for descending.")
                return
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    print("Sorted prices:", arr)
    
if __name__ == '__main__':
    price_array = []
    num = int(input("Enter number of books: "))
    for _ in range(num):
        val = int(input("Enter price of book: "))
        price_array.append(val)
    price_sort(price_array)

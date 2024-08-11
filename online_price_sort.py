def online_price_sort(arr):
    l = len(arr)
    choice = int(input('Do you want asc(1) or desc(2): '))    
    
    for i in range(l):
        for j in range(l-1):
            if choice == 1:
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
            elif choice == 2:
                if arr[j] < arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
    print("Prices in sorted order")
    print(arr)
    
    
if __name__ == "__main__":
    price_array = []
    num = int(input("Enter number of items: "))
    for _ in range(num):
        val = int(input("Enter price of items: "))
        price_array.append(val)
    online_price_sort(price_array)
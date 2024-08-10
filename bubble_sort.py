def bubble_sort(arr,l):
    for i in range(l):
        for j in range(l-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

if __name__ == '__main__':
    arr = list()
    n = int(input("Enter no elements: "))
    for _ in range(n):
        val = int(input("Enter value: "))
        arr.append(val)
    bubble_sort(arr,n)